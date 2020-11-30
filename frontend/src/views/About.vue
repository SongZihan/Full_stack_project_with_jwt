<template>
  <div class="about">
    <h1>This is an about page</h1>
    <el-button @click="get_somedata">This is a button</el-button>
    <el-form :model="ruleForm" status-icon ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="username">
        <el-input  v-model="ruleForm.username" autocomplete="on"></el-input>
      </el-form-item>
      <el-form-item label="password" type="password">
        <el-input v-model="ruleForm.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">login</el-button>
      </el-form-item>
    </el-form>
    <el-button @click="test_login">Test login</el-button>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      ruleForm: {
        username: '',
        password: ''
      }
    }
  },
  methods:{
    // 버튼을 클릭 한 후 트리거되는 함수
    get_somedata(){
      this.$axios({
        method: 'get',
          url: '/get_something'
      }).then( res => {
        console.log('response msg is ' + res.data.msg)
        console.log('response data is ' + res.data.data)

        this.$message({
                  message: 'Successfully get data!' + res.data.msg,
                  type: 'success',
                  showClose: true,
                  duration: 1000
                })
      })
    },
    submitForm(){
      this.$axios({
        method: 'post',
        url: '/login',
        data: this.ruleForm
      }).then( res => {
        console.log('response msg is ' + res.data.msg)
        console.log('response data is ' + res.data.data)

        this.$message({
                  message: 'Successfully get data!' + res.data.msg,
                  type: 'success',
                  showClose: true,
                  duration: 1000
                })
        // jwt를 처리한다
        console.log('jwt token is ' + res.data.jwt_token)
        sessionStorage.jwt_token = res.data.jwt_token



      }).catch( error => {
        this.$message({
                  message: 'error login',
                  type: 'error',
                  showClose: true,
                  duration: 1000
                })
      })
    },
    test_login(){
      console.log('jwt token is ' + sessionStorage.getItem('jwt_token') )
      this.$axios({
        method: 'get',
        url: '/test_login',
        headers: {'Authorization': sessionStorage.getItem('jwt_token') },
      }).then( res => {
        console.log('response msg is ' + res.data.msg)
        console.log('response data is ' + res.data.data)

        this.$message({
                  message: 'Successfully get data!' + res.data.msg,
                  type: 'success',
                  showClose: true,
                  duration: 1000
                })

      }).catch( error => {
        this.$message({
                  message: 'error login',
                  type: 'error',
                  showClose: true,
                  duration: 1000
                })
      })
    }
  }
}
</script>
