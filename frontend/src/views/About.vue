<template>
  <div class="about">
    <h1>This is an about page</h1>
    <el-button @click="get_somedata">This is a button</el-button>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {

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
    }
  }
}
</script>
