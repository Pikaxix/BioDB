<template>
  <el-container class="itempage-container">
    <el-main>
      <div class="breadcrum">
        <!-- breadcrumb -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/microbe' }">Microbe</el-breadcrumb-item>
          <el-breadcrumb-item>{{ this.$route.params.genome_name }}</el-breadcrumb-item>
        </el-breadcrumb>
      </div>

      <div class="general-card">
        <!--General card -->
        <el-card>
          <el-divider content-position="left">
            <h5>General</h5>
          </el-divider>
          <el-row :gutter="4">
            <el-col :span="5" :offset="2">
              <div class="Infotag">Genome Name</div>
              <div class="Infotag">Assembly Accession</div>
              <div class="Infotag">Organism</div>
              <div class="Infotag">LOCUS</div>
              <div class="Infotag">Length</div>
              <div class="Infotag">Type</div>
              <div class="Infotag">Systems</div>
            </el-col>
            <el-col :span="10">
              <div>{{ basic_data.genome_name }}</div>
              <div>{{ basic_data.assembly_accession }}</div>
              <div>{{ basic_data.organism }}</div>
              <div>{{ basic_data.LOCUS }}</div>
              <div>{{ basic_data.length }}</div>
              <div>{{ basic_data.type }}</div>
              <div>
                <el-tag v-for="item in systems_list" :key="item" type>{{ item }}</el-tag>
              </div>
            </el-col>
          </el-row>
        </el-card>
      </div>
      <el-divider></el-divider>
      <p></p>
      <div class="systems">
        <el-card>
          <div class="systems">
            <div class="CRISPR" v-if="IsShow['CRISPR']">
              <el-divider content-position="left">CRISPR</el-divider>
              <div v-for="item in systems_data['CRISPR']" :key="item.Repeat">
                <span class="sub_title_s">{{ item.Repeat }}</span>
                <el-row :gutter="4">
                  <el-col :span="5" :offset="5">
                    <div class="Infotag">Position</div>
                    <div class="Infotag">Subtype</div>
                    <div class="Infotag">Superclass</div>
                    <div class="Infotag">Families</div>
                    <div class="Infotag">motif_structures</div>
                  </el-col>
                  <el-col :span="10">
                    <div>{{ item.Position }}</div>
                    <div>{{ item.Subtype }}</div>
                    <div>{{ item.Families }}</div>
                    <div>{{ item.Position }}</div>
                    <div>{{ item.motif_structures }}</div>
                  </el-col>
                </el-row>
                <p></p>
              </div>
            </div>
            <div class="RM" v-if="IsShow['RM']">
              <el-divider content-position="left">RM</el-divider>
              <div v-for="item in systems_data['RM']" :key="item.protein">
                <span class="sub_title_s">{{ item.protein }}</span>
                <el-row :gutter="4">
                  <el-col :span="5" :offset="5">
                    <div class="Infotag">Type</div>
                    <div class="Infotag">Protein</div>
                    <div class="Infotag">Annotation</div>
                  </el-col>
                  <el-col :span="10">
                    <div>{{ item.type }}</div>
                    <div>{{ item.protein }}</div>
                    <div>{{ item.annotation }}</div>
                  </el-col>
                </el-row>
                <p></p>
              </div>
            </div>
            <div class="Abi" v-if="IsShow['Abi']">
              <el-divider content-position="left">Abi</el-divider>
              <div v-for="item in systems_data['Abi']" :key="item.protein">
                <span class="sub_title_s">{{ item.protein }}</span>
                <el-row :gutter="4">
                  <el-col :span="5" :offset="5">
                    <div class="Infotag">Protein</div>
                    <div class="Infotag">Annotation</div>
                  </el-col>
                  <el-col :span="10">
                    <div>{{ item.protein }}</div>
                    <div>{{ item.annotation }}</div>
                  </el-col>
                </el-row>
                <p></p>
              </div>
            </div>
            <div class="BREX" v-if="IsShow['BREX']">
              <el-divider content-position="left">BREX</el-divider>
              <div v-for="item in systems_data['BREX']" :key="item.protein">
                <span class="sub_title_s">{{ item.protein }}</span>
                <el-row :gutter="4">
                  <el-col :span="5" :offset="5">
                    <div class="Infotag">Protein</div>
                    <div class="Infotag">Annotation</div>
                  </el-col>
                  <el-col :span="10">
                    <div>{{ item.protein }}</div>
                    <div>{{ item.annotation }}</div>
                  </el-col>
                </el-row>
                <p></p>
              </div>
            </div>
            <div class="pAgos" v-if="IsShow['pAgos']">
              <el-divider content-position="left">pAgos</el-divider>
              <div v-for="item in systems_data['pAgos']" :key="item.protein">
                <span class="sub_title_s">{{ item.protein }}</span>
                <el-row :gutter="4">
                  <el-col :span="5" :offset="5">
                    <div class="Infotag">Protein</div>
                    <div class="Infotag">Annotation</div>
                  </el-col>
                  <el-col :span="10">
                    <div>{{ item.protein }}</div>
                    <div>{{ item.annotation }}</div>
                  </el-col>
                </el-row>
                <p></p>
              </div>
            </div>
            <div class="TA" v-if="IsShow['TA']">
              <el-divider content-position="left">TA</el-divider>
              <div v-for="item in systems_data['TA']" :key="item.protein">
                <span class="sub_title_s">{{ item.protein }}</span>
                <el-row :gutter="4">
                  <el-col :span="5" :offset="5">
                    <div class="Infotag">Type</div>
                    <div class="Infotag">Protein</div>
                    <div class="Infotag">Annotation</div>
                  </el-col>
                  <el-col :span="10">
                    <div>{{ item.type }}</div>
                    <div>{{ item.protein }}</div>
                    <div>{{ item.annotation }}</div>
                  </el-col>
                </el-row>
                <p></p>
              </div>
            </div>
          </div>
        </el-card>
      </div>
    </el-main>
  </el-container>
</template>

<script>
export default {
  props: {
    microbe_nowTab: String
  },
  data () {
    return {
      queryInfo: {
        genome_name: ''
      },
      system_name: '',
      basic_data: [],
      systems_data: [],
      systems_list: [],
      IsShow: {
        CRISPR: false,
        RM: false,
        Abi: false,
        TA: false,
        pAgos: false,
        BREX: false
      }
    }
  },
  created () {
    this.queryInfo.genome_name = this.$route.params.genome_name
    this.system_name = this.$route.path
      .substr(1)
      .replace('/itempage', '')
      .toUpperCase()
    this.getGenomeInfo()
  },
  methods: {
    getGenomeInfo () {
      var path = 'genomeInfo'
      this.axios
        .get(path, { params: this.queryInfo })
        .then(res => {
          this.basic_data = res.data.basic_data
          this.systems_data = res.data.systems_data
          this.systems_list = res.data.systems_list
          this.InitIsshow()
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    InitIsshow () {
      for (var i = 0; i < this.systems_list.length; i++) {
        this.IsShow[this.systems_list[i]] = true
      }
    },
    handleBreadClick () {
      history.back()
    }
  }
}
</script>

<style lang="less" scoped>
.itempage-container {
  padding: 0px 100px 0px 100px;
  background-color: #ccff9950;
}
.el-divider {
  margin-top: 10px;
}
.Infotag {
  font-weight: 500;
}
</style>
