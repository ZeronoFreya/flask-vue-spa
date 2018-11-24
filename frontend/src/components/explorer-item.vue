<template>
    <li>
        <label
            @click="open(model)">{{model.name}}</label>
        <ul v-if='model.isFolder'>
            <explorer-item v-for="(item,i) in model.children" :key="i"
                :model.sync="item" :num.sync="i"
                :openfolder="openfolder"
                :trees.sync="trees"></explorer-item> 
        </ul>
    </li>
</template>
<script>
export default {
    name:"explorerItem",
    props:{
        model: {
            type: Object,
            twoWay: true,
        },
        num:{
            type: Number,
            twoWay: true,
        },
        trees: {
            type: Array,
            twoWay: true,
            default: [],
        },
        openfolder: {
            type: Function,
        },
    },
    methods:{
        getParentNode(m, cb) {
            // 查找点击的子节点
            var recurFunc = (data, list) => {
                data.forEach(i => {
                    if (i.id == m.id) {
                        this.parentNodeModel = list;
                        return;
                    }
                    
                    if (i.children) {
                        typeof cb == "function" && cb.call(i.children);
                        recurFunc(i.children, i);
                    }
                });
            };
            recurFunc(this.trees, this.trees);
        },
        getPath(m){
            let pathArray = m.path.split(',')
            let idx = 0
            let path = ''
            let f = (data) => {
                data.forEach(i=>{
                    if (i.id == pathArray[idx]) {
                        path += i.name + '\\'
                        if (i.id == m.id) {
                            return
                        }
                        idx++
                    }
                    if (i.children) {
                        f(i.children)
                    }
                })
            }
            f(this.trees)
            
            return path;
        },
        open(m){
            console.log(m.id,m.parentId,m.path);
            // this.getParentNode(m,null)
            // console.log(this.parentNodeModel.name);
            // var path = this.getPath(m)
            // console.log(path)
            
            if (m.hasOwnProperty("children")){
                // console.log(12);
                
                if (!m.isExpand) {                    
                    // this.expandFolder(m,p)
                    if (typeof this.openfolder == "function") {
                        let path = this.getPath(m)
                        this.openfolder.call(null, m, path);
                    }
                    m.isExpand = true
                }
                
            }
        }
    }
}
</script>
