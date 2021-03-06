
const path = require('path')

module.exports = {
  chainWebpack: config => {
    config.resolve.alias
      .set('@', path.resolve(__dirname, 'src/'))
      
  },
  css: {
    loaderOptions: {
      scss: {
        additionalData: `@import "src/assets/scss/colors.scss";`
      }
    }
  }
}