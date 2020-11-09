
const path = require('path')

module.exports = {
  // 출력 파일 디렉토리
  assetsDir: '../static', // 출력 정적 파일 위치（outputdir에 상대적）
  // publicPath: '/',
  outputDir: path.resolve(__dirname, '../backend/templates'), // index.html 항목 파일 위치


  chainWebpack: () => {},
  configureWebpack: () => {},

  devServer: {
    open: process.platform === 'darwin',
    host: 'localhost',
    port: 9099,
    https: false,
    hotOnly: false,
    proxy: { // 도메인 간 문제 해결
      '/': {
        target: 'http://localhost:5000', // target
        ws: true,
        changOrigin: true // 교차 도메인 허용
      }
    }, // 设置代理
    before: app => {}
  },
  // 第三方插件配置
  pluginOptions: {
    // ...
  }
}
