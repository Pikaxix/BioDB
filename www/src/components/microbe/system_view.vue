<template>
  <div>
    <!-- Navi -->
    <!-- <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/microbe' }">Microbe</el-breadcrumb-item>
      <el-breadcrumb-item>{{system_name}}</el-breadcrumb-item>
    </el-breadcrumb>-->
    <!-- Card -->
    <el-card class="box-card">
      <!-- Search Bar
      <el-row>
        <el-col :span="10">
          <el-input placeholder="Search"
          v-model="queryInfo.query" class="input-with-select">
            <el-select v-model="queryInfo.select" slot="prepend" placeholder="Select" style="width:110px">
              <el-option label="Genome" value="genome_name"></el-option>
              <el-option label="Organism" value="organism"></el-option>
              <el-option label="LOCUS" value="LOCUS"></el-option>
            </el-select>
            <el-button slot="append" icon="el-icon-search" @click="getSystemItem"></el-button>
          </el-input>
        </el-col>
        <el-col :span="4"></el-col>
      </el-row>-->

      <!-- Router view -->
      <router-view ></router-view>

      <!-- Table -->
      <el-table :data="sys_item" style="width: 100%" @row-click="handleItemPage" v-if="IsShowTale">
        <el-table-column type="index"></el-table-column>
        <el-table-column prop="genome_name" label="Genome Name"></el-table-column>
        <el-table-column prop="organism" label="Organism"></el-table-column>
        <el-table-column prop="LOCUS" label="LOCUS"></el-table-column>
      </el-table>

      <!-- pagination -->
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="queryInfo.pagenum"
        :page-sizes="[5, 10, 20, 40]"
        :page-size="queryInfo.pagesize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="sys_total"
      ></el-pagination>
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      // GET 参数
      queryInfo: {
        query: '',
        select: '',
        pagenum: 1,
        pagesize: 10
      },

      sys_item: [],
      sys_total: 0,
      system_name: '',
      IsShowTale: false
    }
  },
  created () {
    this.system_name = this.$route.params.system
    this.getSystemItem()
  },
  methods: {
    getSystemItem () {
      var path = 'systems/' + this.system_name
      this.axios
        .get(path, { params: this.queryInfo })
        .then(res => {
          this.sys_item = res.data.data
          this.sys_total = res.data.total
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    handleSizeChange (newSize) {
      this.queryInfo.pagesize = newSize
      this.getSystemItem()
    },
    handleCurrentChange (newPage) {
      this.queryInfo.pagenum = newPage
      this.getSystemItem()
    },
    handleItemPage (row, event, column) {
      this.IsShowTable = false
      this.$router.push({
        path: this.$route.path + `/itempage/${this.system_name}`,
        query: {
          genome_name: row.genome_name
        }
      })
    }
  }
}
</script>

<style lang="less" scoped>
</style>
