<template>
    <li :class="liClassVal">
        <span :class="spanClassVal" @click='open(model)'></span>
        <a  @mouseenter='enterFunc(model)' @mouseleave='leaveFunc(model)'  @contextmenu.prevent='cxtmenufunc(model)'>
            <span :class="{loadSyncNode:model.loadNode==1}" v-if='model.loadNode==1'></span>
            <span :class='model.iconClass' v-show='model.iconClass' v-else></span>
            <span v-show='ischeck' id="treeDemo_5_check" class="button chk" :class='{"checkbox_false_full":!model.ckbool,"checkbox_true_full":model.ckbool}' @click='ckFunc(model)' treenode_check=""></span>
            <span class="node_name" :class='aClassVal' @click='Func(model),open(model)' >{{model.name}}</span>

            <!--删除-->
            <span v-show='model.hover' title='删除' class="button remove" @click="delNode(model)"></span>
        </a>
        <ul :class="ulClassVal" v-show='model.isFolder'>
            <ztree-item v-for="(item,i) in model.children" :key='i' 
            :callback='callback' :expandfunc='expandfunc' :cxtmenufunc='cxtmenufunc' 
            :model.sync="item" :num.sync='i' root='1' :nodes.sync='model.children.length' 
            :ischeck='ischeck' :trees.sync='trees'></ztree-item>
        </ul>
    </li>
</template>
<script>
export default {
    name: "ztreeItem",
    data() {
        return {
            parentNodeModel: null,
        };
    },
    props: {
        model: {
            type: Object,
            twoWay: true,
        },
        num: {
            type: Number,
            twoWay: true,
        },
        nodes: {
            type: Number,
            twoWay: true,
            default: 0,
        },
        trees: {
            type: Array,
            twoWay: true,
            default: [],
        },
        root: {
            type: String,
            twoWay: true,
        },
        callback: {
            type: Function,
        },
        expandfunc: {
            type: Function,
        },
        cxtmenufunc: {
            type: Function,
        },
        ischeck: {
            type: Boolean,
            twoWay: true,
            default: false,
        },
    },
    methods: {
        Func(m) {
            // 查找点击的子节点
            var recurFunc = (data, list) => {
                data.forEach(i => {
                    if (i.id == m.id) {
                        i.clickNode = true;
                        if (typeof this.callback == "function") {
                            this.callback.call(null, m, list, this.trees);
                        }
                    } else {
                        i.clickNode = false;
                    }

                    if (i.children) {
                        recurFunc(i.children, i);
                    }
                });
            };

            recurFunc(this.trees, this.trees);
        },
        ckFunc(m) {
            m.ckbool = !m.ckbool;

            // 查找复选框的所有子节点
            var recurFuncChild = data => {
                data.forEach(i => {
                    i.ckbool = m.ckbool;
                    if (i.children) recurFuncChild(i.children);
                });
            };
            recurFuncChild(m.children);

            // 查找复选框的所有父节点
            var parentId = m.parentId;
            var recurFuncParent = (data, list) => {
                data.forEach(i => {
                    if (i.id == parentId && parentId > 0) {
                        parentId = i.parentId;
                        // 判断父亲节点的儿子节点选中个数
                        var childrenCks = i.children.filter(child => {
                            return child.ckbool == true;
                        });
                        // 如果大于0, 证明不能取消选中状态
                        i.ckbool = childrenCks.length > 0;
                        // 递归查找
                        recurFuncParent(this.trees, i);
                    } else if (i.id == m.id && i.parentId == 0) {
                        i.ckbool = m.ckbool;
                        isFindRootBool = true;
                    } else {
                        recurFuncParent(i.children, i);
                    }
                });
            };
            recurFuncParent(this.trees, this.trees);
        },
        getParentNode(m, cb) {
            // 查找点击的子节点
            var recurFunc = (data, list) => {
                data.forEach(i => {
                    if (i.id == m.id) this.parentNodeModel = list;
                    if (i.children) {
                        typeof cb == "function" && cb.call(i.children);
                        recurFunc(i.children, i);
                    }
                });
            };
            recurFunc(this.trees, this.trees);
        },
        open(m) {
            //
            m.isExpand = !m.isExpand;

            if (typeof this.expandfunc == "function" && m.isExpand) {
                if (m.loadNode != 2) {
                    //
                    this.expandfunc.call(null, m);
                } else {
                    m.isFolder = !m.isFolder;
                }
            } else {
                m.isFolder = !m.isFolder;
            }
        },
        enterFunc(m) {
            m.hover = true;
            this.getParentNode(m, null);
        },
        leaveFunc(m) {
            m.hover = false;
        },
        // 删除节点
        delNode(nodeModel) {
            if (nodeModel) {
                if (this.parentNodeModel.hasOwnProperty("children")) {
                    this.parentNodeModel.children.splice(
                        this.parentNodeModel.children.indexOf(nodeModel),
                        1,
                    );
                } else if (this.parentNodeModel instanceof Array) {
                    // 第一级根节点处理
                    this.parentNodeModel.splice(
                        this.parentNodeModel.indexOf(nodeModel),
                        1,
                    );
                }
                nodeModel = null;
            } else {
                console.log("请先选中节点");
            }
        },
        
    },
    computed: {
        // 给（根 和 子树）赋值不同的样式
        rootClass() {
            var strRootClass = "";

            // 根判断
            if (this.root == "0") {
                this.model.children = this.model.children || [];
                strRootClass =
                    this.num == 0 && this.model.children.length == 0
                        ? "roots_docu"
                        : this.nodes == 1 ||
                          (this.num == 0 && this.nodes != this.num + 1)
                            ? "root_"
                            : this.nodes == this.num + 1
                                ? "bottom_"
                                : "center_";

                // 子树判断
            } else if (this.root == "1") {
                this.model.children = this.model.children || [];
                strRootClass =
                    this.nodes > 1 &&
                    this.model.children.length > 0 &&
                    this.nodes != this.num + 1
                        ? "center_"
                        : (this.num == 0 && this.nodes > 1) ||
                          this.nodes != this.num + 1
                            ? "center_docu"
                            : (this.nodes == 1 && this.num != 0) ||
                              (this.nodes == this.num + 1 &&
                                  this.model.children.length > 0)
                                ? "bottom_"
                                : "bottom_docu";
            }

            return strRootClass;
        },
        // 是否有儿子节点
        isChildren() {
            return this.num + 1 != this.nodes;
        },
        // 展开/收起
        prefixClass() {
            var returnChar = "";
            if (this.rootClass.indexOf("docu") == -1) {
                if (this.model.isFolder) {
                    returnChar = "open";
                } else {
                    returnChar = "close";
                }
            }

            if (
                this.model.children.length == 0 &&
                this.rootClass.indexOf("docu") == -1
            ) {
                returnChar = "docu";
            }

            return returnChar;
        },
        liClassVal() {
            return "level" + this.num;
        },
        spanClassVal() {
            return (
                "button level" +
                this.num +
                " switch " +
                this.rootClass +
                this.prefixClass
            );
        },
        aClassVal() {
            return this.model.clickNode
                ? "level" + this.num + " curSelectedNode"
                : "level" + this.num;
        },
        ulClassVal() {
            return this.isChildren && this.model.children.length > 0
                ? "level" + this.num + " line"
                : "level" + this.num;
        },
    },
};
</script>
