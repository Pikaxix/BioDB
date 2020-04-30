<template>
  <el-container class="homecontainer">
    <el-header height="90px">
      <div class="logobox">
        <router-link tag="a" to='/home'>
        <img src="./assets/imgs/lab-logo.png" alt />
        </router-link>
      </div>
      <el-input placeholder="Search" v-model="Search"></el-input>
      <el-menu
        :default-active="$route.path"
        class="menu-box"
        mode="horizontal"
        background-color="#FFFFFF"
        text-color="#000000"
        active-text-color="#3a8eda"
        router
      >
        <el-menu-item index="/home">
          <i class="el-icon-s-home"></i>
        </el-menu-item>
        <el-menu-item index="/microbe">Microbe</el-menu-item>
        <el-menu-item index="/phage">Phage</el-menu-item>
        <el-submenu index="3">
          <template slot="title">Functions</template>
          <el-menu-item index="motherboard">S1</el-menu-item>
          <el-menu-item index="2-2">S2</el-menu-item>
          <el-menu-item index="2-3">S3</el-menu-item>
        </el-submenu>
        <el-menu-item index="/help">Help</el-menu-item>
      </el-menu>
    </el-header>
    <!-- Herader -->
    <el-container>
      <router-view></router-view>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      Search: ''
    }
  }
}
</script>

<style lang="less" scoped>
.homecontainer {
  height: 100vh;
}
.el-header {
  background-color: #ffffff;
  display: flex;
  .logobox {
    height: 50px;
    width: 50px;
    position: relative;
    top: 20%;
    left: 5%;
    img {
      height: 100%;
      widows: 100%;
    }
  }
  .el-input{
    width: 300px;
    position: relative;
    left: 25%;
    top: 30%

  }
  .el-menu {
    width: 500px;
    position: relative;
    left: 33%;
    top: 15%;
    height: 40px;
    .el-menu-item {
      font-size: 17px;
    }
    /deep/ .el-submenu .el-submenu__title {
      font-size: 17px;
    }
  }
}
</style>
