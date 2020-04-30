#-------------------------------------------------------------------------------
# Name:         microbe.py
# Description:  
# Author:       zhnmozhang@gmail.com--EP45-DS3L
# Date:         2020/3/17  23:54
#-------------------------------------------------------------------------------

from . import api
from . import Mongodb
from flask import jsonify,request,make_response

@api.route("/systems",methods=['GET'])
def systems():
    """GET system view"""
    find = Mongodb.db.systems.find()
    result = []
    for it in find:
        result.append({
            'system_id': it['system_id'],
            'system_name': it['system_name'],
            'bacteria_num': it['bacteria_num'],
            'system_desc': it['system_desc']
            })
    return jsonify({"data":result})


@api.route("/all_microbe", methods = ['POST'] )
def get_all_microbe():
    # get query param*s setting
    pageInfo = request.json['pageInfo']
    select = list(request.json['select'])
    pagenum = pageInfo["pagenum"]
    pagesize = pageInfo["pagesize"]
    skipnum = int(int(pagenum) - 1) * int(pagesize)

    # other query info
    collection = Mongodb.db.gbff
    all_systems = list(Mongodb.db.systems.find({}, {'_id': 0, 'system_name': 1}))

    # query handling
    gbff_search = []
    if(select[0] == 'All'):
        gbff_search = (list(collection.find({}, {'_id': 0})))
    else:
        for sys in select:
            gbff_search += list(collection.find({str.lower(sys) : True}, {'_id': 0}))

    result = []
    total = len(gbff_search)
    for it in gbff_search[skipnum:int(pagesize) + skipnum]:
        systems_list = []
        for i in all_systems:
            if (it[str.lower(i['system_name'])]):
                systems_list.append(i['system_name'])

        result.append({
            'genome_name': it['genome_name'],
            'LOCUS': it['LOCUS'],
            'organism': it['organism'],
            'systems': systems_list
        })

    return jsonify({
        'Total': total,
        'Data': result
    })


@api.route("/systems/<systemname>",methods=['GET'])
def view_system(systemname):
    pagenum = request.args.get("pagenum")
    pagesize = request.args.get("pagesize")
    query = request.args.get("query")
    select = request.args.get("select")
    collection = Mongodb.db.gbff
    skipnum = int(int(pagenum) - 1) * int(pagesize)
    if( query!='' and select != '' ):
        if(select == 'organism' or select == 'genome_name'):
            search = collection.find({select:{'$regex': query},systemname: True})
        else:
            search = collection.find({select: query,systemname:True})
    else:
        search = collection.find({systemname:True})
    result = []
    for it in search[skipnum:int(pagesize)+skipnum]:
        result.append({
            'genome_name': it['genome_name'],
            'LOCUS': it['LOCUS'],
            'organism': it['organism']
        })
    total = search.count()
    return jsonify({
        'total': total,
        'data': result
    })

@api.route("/genomeInfo",methods=['GET'])
def GenomeInfo():
    genome_name = request.args.get("genome_name")
    gbff_collection = Mongodb.db['gbff']
    all_systems=Mongodb.db.systems.find({},{'_id':0,'system_name':1})
    gbff_search = gbff_collection.find_one({'genome_name':genome_name}, {'_id':0 })
    assembly_accession = gbff_search['assembly_accession']
    systems_data = {}
    systems_list = []

    for it in all_systems:
        if(gbff_search[str.lower(it['system_name'])]):
            systems_list.append(it['system_name'])
            sys_collection = Mongodb.db[str.lower(it['system_name'])]
            sys_sets=[]
            for each in sys_collection.find({'assembly_accession':assembly_accession},{'_id':0}):
                sys_sets.append(each)

            systems_data[it['system_name']]=sys_sets

    return jsonify({
        'basic_data':gbff_search,
        'systems_list':systems_list,
        'systems_data':systems_data
    })
