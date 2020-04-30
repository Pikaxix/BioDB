<template>
  <el-container class="microbe-container">
    <el-main>
      <div class="intro">
        <div>
          <h3>Microbe Dataset</h3>
          <el-divider></el-divider>
          <div style=" padding:10px;">
            <h3>All of the 14,407 available samples In our database:</h3>
            <div
              style="text-indent: 1em"
            >We divide them into 6 categories by different anti-phage immune systems.</div>
            <div
              style="text-indent: 1em"
            >On this page, we provide an overview of the data available within our database.</div>
          </div>
        </div>
      </div>
      <el-divider></el-divider>
      <p></p>
      <div class="radio">
        <el-radio v-model='All' label="All" border @change="HandleTabClick">All</el-radio>
        <el-checkbox-group v-model="nowTab" @change="HandleTabClick">
          <el-checkbox
            v-for="item in sys_list"
            :key="item.system_id"
            :label="item.system_name"
            border
          >{{ item.system_name }}</el-checkbox>
        </el-checkbox-group>
      </div>
      <el-divider></el-divider>
      <!-- Search Bar -->
      <div class="search">
        <el-row>
          <el-col :span="24">
            <el-input placeholder="Search" v-model="pageInfo.query" class="input-with-select">
              <el-select
                v-model="pageInfo.select"
                slot="prepend"
                placeholder="Select"
                style="width:150px"
              >
                <el-option label="Genome" value="genome_name"></el-option>
                <el-option label="Organism" value="organism"></el-option>
                <el-option label="LOCUS" value="LOCUS"></el-option>
              </el-select>
              <el-button slot="append" icon="el-icon-search" @click="getSearchItem"></el-button>
            </el-input>
          </el-col>
          <el-col :span="10"></el-col>
        </el-row>
      </div>
      <p></p>
      <div class="dataset">
        <!-- Router view -->
        <router-view :key="$route.fullPath"></router-view>
        <!-- All Table -->
        <el-table :data="Result_List" style="width: 100%" key="all"  v-loading="loading">
          <el-table-column label="Genome Name" width="350px">
            <template slot-scope="props">
              <router-link tag="a" target="_blank" :to="'/itempage/'+ props.row.genome_name">
                <a>
                  <i class="el-icon-s-promotion"></i>
                  {{ props.row.genome_name }}
                </a>
              </router-link>
              <!-- <el-button >ncbi</el-button> -->
            </template>
          </el-table-column>
           <el-table-column label="Organism" prop="organism" width="230px"></el-table-column>
          <el-table-column label="LOCUS" prop="LOCUS" width="90px"></el-table-column>
          <el-table-column label="Systems" width="205px">
            <template slot-scope="props">
              <el-tag v-for="item in props.row.systems" :key="item" type>{{ item }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column label="Phage" width="220px"></el-table-column>
          <el-table-column label="Link to" width="80px">
            <template slot-scope="props">
              <a :href="'https://www.ncbi.nlm.nih.gov/nuccore/'+ props.row.LOCUS" target="_blank">
                NCBI
                <i class="el-icon-top-right"></i>
              </a>
              <!-- <el-button >ncbi</el-button> -->
            </template>
          </el-table-column>
        </el-table>
        <!-- pagination -->
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="pageInfo.pagenum"
          :page-sizes="[5, 10, 20, 40]"
          :page-size="pageInfo.pagesize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="Total"
        ></el-pagination>
      </div>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      sys_list: [],
      Result_List: [],
      Total: 0,
      All: 'All',
      nowTab: [],
      select: [],
      pageInfo: {
        pagenum: 1,
        pagesize: 10
      },
      loading: true,
      system_name: ''
    }
  },
  created () {
    this.getSystemsList()
    this.getResultlist()
  },
  methods: {
    getSearchItem () {
      var path = 'systems/' + this.system_name
      this.axios
        .get(path, { params: this.pageInfo })
        .then(res => {
          this.all_list = res.data.data
          this.total = res.data.total
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    getSystemsList () {
      this.axios
        .get('systems')
        .then(res => {
          this.sys_list = res.data.data
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    getResultlist () {
      // eslint-disable-next-line eqeqeq
      if (this.All == 'All') {
        this.select = ['All']
      } else {
        this.select = this.nowTab
      }
      this.axios({
        url: 'http://api.dacapo.top/api/all_microbe',
        method: 'post',

        data: {
          pageInfo: this.pageInfo,
          select: this.select
        },
        header: {
          'Content-Type': 'application/json' // 如果写成contentType会报错
        }
      })
        .then(res => {
          this.Result_List = res.data.Data
          this.Total = res.data.Total
          this.loading = false
        })
        .catch(error => {
          console.log(error)
        })
    },
    getSystemItem () {
      var path = 'systems/' + this.system_name
      this.axios
        .get(path, { params: this.pageInfo })
        .then(res => {
          this.all_list = res.data.data
          this.sys_total = res.data.total
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    HandleTabClick (tab) {
      // eslint-disable-next-line eqeqeq
      if (tab == 'All') {
        this.nowTab = []
        this.select = []
        this.All = 'All'
        this.select = ['All']
        this.loading = true
      } else {
        this.All = ''
        this.select = this.nowTab
        this.loading = true
      }
      this.getResultlist()
    },
    handleSizeChange (newSize) {
      this.pageInfo.pagesize = newSize
      // eslint-disable-next-line eqeqeq
      this.getResultlist()
    },
    handleCurrentChange (newPage) {
      this.pageInfo.pagenum = newPage
      this.getResultlist(this.nowTab)
    }
    // handleItemPage (row, event, column) {
    //   this.IsShowTable = false
    //   this.IsShowTable_All = false
    //   this.$router.push({
    //     path: this.$route.path + `/itempage/${this.nowTab}`,
    //     query: {
    //       genome_name: row.genome_name
    //     }
    //   })
    // }

  }
}
</script>

<style lang="less" scoped>
.microbe-container {
  padding: 0px 100px 0px 100px;
  background-color: #99ccff20;
}
</style>
