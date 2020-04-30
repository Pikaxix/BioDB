<template>
  <el-container class="home-container">
    <el-main>
      <div class="intro" style="height:200px">
        <div>
          <h3>Microbe DB</h3>
          <el-divider></el-divider>
          <div style=" padding:10px;">
            <h3>Motivating questions in this database include：</h3>
            <div style="text-indent: 1em">· Common microbial immune systems</div>
            <div style="text-indent: 1em">· What dictates the evolution of microbial immune system?</div>
            <div
              style="text-indent: 1em"
            >· Ultimately, we intend to leverage this information to rationally analyze microbial immune systems.</div>
          </div>
        </div>
      </div>
      <br />
      <el-divider></el-divider>
      <!-- Research Info -->
      <div class="our-research" style="height:500px">
        <h3>Our Research</h3>
        <div style=" padding:15px;float:left">
          <el-card
            style="
              padding:15px;
              width: 420px;
              height: 400px;
              background-color: #1d6896;"
          >
            <p
              style="font-size: 20px;color:white"
            >Research in the Chen's Lab is directed towards the XXXX</p>
            <p></p>
            <p style="font-size: 20px;color:white">
              We employ a comprehensive approach to collect and analyze 14,407 samples,
              developing a valid dataset of the microbial immune systems.
            </p>
          </el-card>
        </div>
        <div
          style="
       display: inline;
       float: right;
       width: 55%;
       position: relative;
       top: 70px;
       "
        >
          <ve-pie :data="chartData" :settings="chartSettings" :legend-visible="false"></ve-pie>
        </div>
      </div>
      <br />
      <!-- Features -->
      <div class="features" style="height:600px">
        <h3>Fearures</h3>
        <div style=" padding:15px;">
          <el-card
            shadow="never"
            style="
              padding:1px;
              width: 710px;
              height: 200px;
              background-color: #fff;
              float:left;
              "
          >
            <div slot="header" class="clearfix">
              <span style="font-size:19px;font-weight:bold">Microbe</span>
            </div>
            <p>Microbe</p>
            <i class="el-icon-edit"></i>
            <i class="el-icon-share"></i>
            <i class="el-icon-delete"></i>
            <i class="el-icon-edit"></i>
            <i class="el-icon-picture-outline-round"></i>
            <i class="el-icon-help"></i>
          </el-card>
          <el-card
            style="
              padding:1px;
              width: 435px;
              height: 130px;
              background-color: #f3f3f3;
              position: relative;
              float:right;
              top:30px
              "
          >
            <span>We divide 14,407 available samples into 6 categories by different anti-phage immune systems.</span>
          </el-card>

          <el-card
            shadow="never"
            style="
              padding:1px;
              width: 710px;
              height: 200px;
              background-color: #fff;
              float:right;
              position: relative;
              top:30px
              "
          >
            <div slot="header" class="clearfix">
              <span style="font-size:19px;font-weight:bold">Phage</span>
            </div>
            <p >Phage</p>
            <i class="el-icon-edit"></i>
            <i class="el-icon-share"></i>
            <i class="el-icon-delete"></i>
            <i class="el-icon-edit"></i>
            <i class="el-icon-picture-outline-round"></i>
            <i class="el-icon-help"></i>
          </el-card>
          <el-card
            style="
              padding:1px;
              width: 435px;
              height: 130px;
              background-color: #f3f3f3;
              position: relative;
              top:60px
              "
          >
            <span>Introducton of phage</span>
          </el-card>
        </div>
      </div>
      <p></p>
      <!-- search -->
      <!-- <el-tabs type="border-card">
        <el-tab-pane label="Microbe">
          <el-input placeholder="Search" v-model="queryInfo.query" class="input-with-select">
            <el-select
              v-model="queryInfo.select"
              slot="prepend"
              placeholder="Select"
              style="width:110px"
            >
              <el-option label="Genome" value="genome_name"></el-option>
              <el-option label="Organism" value="organism"></el-option>
              <el-option label="LOCUS" value="LOCUS"></el-option>
            </el-select>
            <el-button slot="append" icon="el-icon-search" @click="getSystemItem"></el-button>
          </el-input>
        </el-tab-pane>
        <el-tab-pane label="Phase">Phase Search</el-tab-pane>
        <el-tab-pane label="Others">Others</el-tab-pane>
      </el-tabs>-->
      <br />
      <br />
      <br />
      <br />
      <el-divider></el-divider>
      <!-- Footer -->
      <el-footer>
        <p style="text-align:center">Microbe DB - Copyright © 2020 Chen's Lab.</p>
      </el-footer>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      sys_list: [],
      chartData: {
        columns: ['System', 'Bacteria_num'],
        rows: []
      },
      chartSettings: {
        radius: 175
      }
    }
  },
  created () {
    this.getSystemsList()
  },
  methods: {
    getSystemsList () {
      this.axios
        .get('systems')
        .then(res => {
          for (var j = 0; j < res.data.data.length; j++) {
            var Dat = {}
            Dat.System = res.data.data[j].system_name
            Dat.Bacteria_num = res.data.data[j].bacteria_num
            this.chartData.rows.push(Dat)
          }
          console.log(this.chartData.rows)
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        })
    }
  }
}
</script>

<style lang="less" scoped>
.home-container {
  padding: 0px 100px 0px 100px;
  background-color: #ccccff45;
}
</style>
