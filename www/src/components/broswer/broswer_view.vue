<template>
  <el-table :data="sys_list" style="width: 100%" @row-click="rowClick">
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="NAME">
            <span>{{ props.row.system_name }}</span>
          </el-form-item>
          <el-form-item label="ID">
            <span>{{ props.row.system_id }}</span>
          </el-form-item>
          <el-form-item label="BACTERIA-NUM">
            <span>{{ props.row.bacteria_num }}</span>
          </el-form-item>
          <el-form-item label="DESCRIPTION">
            <span>{{ props.row.system_desc }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column label="SYSTEM" prop="system_name"></el-table-column>
    <el-table-column label="BACTERIA NUM" prop="bacteria_num"></el-table-column>
    <el-table-column label="DESCRIPTION" prop="system_desc"></el-table-column>
  </el-table>
</template>

<style>
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 150px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 100%;
}
</style>

<script>
export default {
  data () {
    return {
      sys_list: []
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
          this.sys_list = res.data.data
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    rowClick (row, event, column) {
      console.log(row.system_name)
    }
  }
}
</script>
