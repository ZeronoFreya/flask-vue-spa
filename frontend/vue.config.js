const path = require("path");
function resolve(dir) {
    return path.join(__dirname, dir);
}
module.exports = {
    lintOnSave: true,
    // 输出文件目录
    outputDir: '../dist',
    // 生产环境是否生成 sourceMap 文件
    productionSourceMap: false,
    baseUrl: process.env.NODE_ENV === "production" ? "./" : "/",
    css: {
        // 开启 CSS source maps ?
        sourceMap: false,
    },
    chainWebpack: config => {
        config.resolve.alias
            .set("@", resolve("src"))
            .set("utils", resolve("src/utils"));
    },
};
