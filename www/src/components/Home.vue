<template>
  <el-container style="height: 700px; border: 1px solid #eee">
    <el-container class="home">
      <el-main>
        <el-card >
          <div slot="header">
             <h1>intro:XXXXXXXXXXXXXXXXXXXXXXX</h1>
          </div>
          <div class="intro">
          <h2>features：</h2>
          <h3>1</h3>
          <h3>2</h3>
          <h3>3</h3>
          </div>
        </el-card>
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <h2>Data Contains</h2>
          </div>
        </el-card>
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <h2>SEARCH</h2>
          </div>
        </el-card>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
</script>

<style lang="less" scoped>
.home{
  padding:0px 100px 0px 100px;
}
.intro{
    background-color: #f5f5f5;
}
</style>
