<template>
    <ul class="explorer">
        <explorer-item
            v-for="(m,i) in treeDataSource" :key="i"
            :model.sync="m" :num.sync="i"
            :openfolder="openFolder"
            :trees.sync="treeDataSource"></explorer-item>        
    </ul>
</template>
<script>
import Vue from 'vue'
import axios from "axios";
import explorerItem from "./explorer-item";
export default {
    name: "explorer",
    data(){
        return{
            treeDataSource:[]
        }
    },
    props: {
        // list:{
        //     type:Array,
        //     twoWay:true
        // },
        target:{
            type:String,
            default:null
        },
        expand:{
            type:Function,
            default:null
        },
        // 是否展开
		isOpen:{
			type:Boolean,
			twoWay:true,
			default:false
		},
    },
    // watch:{
    //     "list":{
    //         handler:function(){
    //             this.initTreeData()
    //         }
    //     }
    // },
    methods:{
        initTreeData(){
            console.log(3);
            
            var tempList = JSON.parse(JSON.stringify(this.list));

            var recurrenceFunc = (data, pid, path) => {
                data.forEach((m)=>{
                    
                    if(!m.hasOwnProperty("clickNode")){
	                    m.clickNode = false;
	                }
                    m.parentId = pid;
                    m.path = path + ',' + m.id

	               	m.loadNode = 0; 
	               	if (m.hasOwnProperty("children")) {
                        recurrenceFunc(m.children,m.id,m.path);
                    } 
                })
            };
            
            recurrenceFunc(tempList,0,'0');

            this.treeDataSource = tempList;
        },
        fun1:function(m,p){
            const path = "http://localhost:5000/api/dl/listdir2";
            axios
                .post(path, {
                    rootDir: p,
                })
                .then(response => {
                    let folders = response.data.folders;
                    let files = response.data.files;
                    let id, c;
                    c = 0;
                    for (let i = 0, j = folders.length; i < j; i++){
                        id = +new Date()+c;
                        m.children.push({
                            id: id,
                            parentId: m.id,
                            name: folders[i],
                            path: m.path+','+id,
                            isExpand: false,
                            isFolder: true,
                            children:[]
                        })
                        c++
                    }
                    for (let i = 0, j = files.length; i < j; i++){
                        id = +new Date()+c;
                        m.children.push({
                            id: id,
                            parentId: m.id,
                            name: files[i],
                            path: m.path+','+id,
                            isFolder: false
                        })
                        c++
                    }
                })
                .catch(error => {
                    console.log(error);
                });
        },
        initDirectory:function(){
            let tempList = [{
                id:0,
                name:this.target,
                path:'0',
                isFolder: true,
                isExpand:false,
                children:[]
            }]
            if (this.isOpen) {
                this.fun1(tempList[0],this.target)
            }
            this.treeDataSource = tempList;
        },
        openFolder:function(m,p){
            console.log(p);
            this.fun1(m,p)
        }
    },
    components:{
        explorerItem,
    },
    mounted(){
        Vue.nextTick(()=>{
            // this.initTreeData();
            this.initDirectory();
        })
    }
};
</script>
<style lang="scss">
.explorer {
    text-align: left;
    .label-wrapper {
        padding-bottom: 10px;
        margin-bottom: 10px;
        // border-bottom: 1px solid #ccc;
        cursor: pointer;
    }
    .label-main{
        padding-left: 30px;
        border-left: 1px #ddd solid;
        margin-left: 6px;
    }
}
</style>

