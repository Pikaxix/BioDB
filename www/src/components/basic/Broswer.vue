<template>
  <el-container style="height: 700px; border: 1px solid #eee">
    <!-- <el-scrollbar>
      <el-aside width="220px">
        <el-menu :default-openeds="['1']"
          active-text-color="#409EFF"
          unique-opened
          router
          :default-active="actiNaviState"
        >
              <el-submenu index="1">
                <template slot="title">
                  <i class="el-icon-location"></i>
                  <span @click="systems" >Microbe</span>
                </template>
                  <el-menu-item
                  index = "/broswer/crispr"
                  v-for="item in sys_list"
                  :key="item.system_id"
                  @click="saveNaviState(system_name)"
                  >
                  {{ item.system_name }}</el-menu-item>
              </el-submenu>
              <el-submenu index="2">
                <template slot="title">
                  <i class="el-icon-location"></i>
                  <span>Phase</span>
                </template>
                  <el-menu-item>
                    1
                  </el-menu-item>
              </el-submenu>
        </el-menu>
      </el-aside>
    </el-scrollbar> -->

    <el-container>
      <el-main>
        <router-view ></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      sys_list: [],
      actiNaviState: ''
    }
  },
  created () {
    this.getSystemsList()
    this.actiNaviState = window.sessionStorage.getItem('savePath')
  },
  methods: {
    getSystemsList () {
      this.axios.get('systems')
        .then((res) => {
          this.sys_list = res.data.data
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    systems () {
      console.log('systems')
    },
    saveNaviState (savePath) {
      window.sessionStorage.setItem('savePath', savePath)
      this.actiNaviState = savePath
    }
  }
}
</script>

<style lang="less" scoped>
.el-aside{
  .el-menu{
    border-right:none
  }
}
</style>
