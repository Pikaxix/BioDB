<template>
  <el-container class="homecontainer">
    <el-header height=90px>
      <div class="logobox">
        <img src="./assets/imgs/lab-logo.png" alt />
      </div>
        <el-menu
          :default-active="$route.path"
          class="menu-box"
          mode="horizontal"
          background-color="#FFFFFF"
          text-color="#000000"
          active-text-color="#E2F0ED"
          router>
          <el-menu-item index="home">Home</el-menu-item>
          <el-menu-item index="broswer">Broswer</el-menu-item>
          <el-menu-item index="research">Research</el-menu-item>
          <el-submenu index="3">
            <template slot="title" >Tools</template>
            <el-menu-item index="motherboard">S1</el-menu-item>
            <el-menu-item index="2-2">S2</el-menu-item>
            <el-menu-item index="2-3">S3</el-menu-item>
          </el-submenu>
          <el-menu-item index="about">Contact</el-menu-item>
        </el-menu>
    </el-header>
    <!-- Herader -->
    <el-container>
        <router-view></router-view>
    </el-container>
  </el-container>
</template>

<script>
</script>

<style lang="less" scoped>
.homecontainer {
  height: 100vh;
}
.el-header {
  background-color: #FFFFFF;
  display: flex;
  .logobox {
    height: 50px;
    width: 50px;
    position: relative;
    top: 20%;
    left:5%;
    img {
      height: 100%;
      widows: 100%;
    }
  }
  .el-menu{
    position: relative;
    left: 55%;
    top: 15%;
    height: 40px;
    .el-menu-item {
      font-size: 17px;
    }
    /deep/ .el-submenu .el-submenu__title{
      font-size: 17px;
    }
  }
}
</style>
