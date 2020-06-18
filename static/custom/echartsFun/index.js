function getToken() {
    let CSRFTokenLi = document.cookie.split('; ').find(v => v.match(/^csrftoken=([^;.]*).*$/))
    return CSRFTokenLi ? CSRFTokenLi.split('=')[1] : ''
}
/**
 *
 * @param {string} echarData.element - 生成echarts图表的标签ID
 * @param {string} echarData.title - echarts的标题
 * @param {list} echarData.dataX - echarts的X轴数据
 * @param {list} echarData.dataY - echarts的Y轴数据
 */
function echartFun(echarData) {
    let myChart = echarts.init(document.getElementById(echarData.element))
    let option = {}
    if(echarData.type == 'pie') {
        let legendData = []
        echarData.data.forEach(val => {
            legendData.push(val.name)
        });
        option = {
            title: {//标题属性
                text: echarData.title, //标题内容
                x: 'center', //标题X轴定位 可用参数 center | left | right | 数字
                y: 0 //标题Y轴定位 可用参数 center | left | right | 数字
            },
            toolbox: {
                feature: {
                    saveAsImage: {}
                }
            },
            tooltip: {//鼠标悬浮层内容
                trigger: 'item', // 悬浮层类型
                formatter: '{a}<br/>{b} : {c} ({d}%)' //自定义悬浮层内容 a：series中的name值 b：对应data的name值 c：对应data的value值 d：对应value值的百分比占比
            },
            legend: {//图例
                orient: 'vertical',
                x: 'left', //图例相对X轴定位center | left | right | 数字
                y: 0, //图例相对Y轴定位 可用参数 center | left | right | 数字
                data: legendData //图例数据  为data的每一项name值组成的列表
            },
            series: [
                {
                    name: '容量：',
                    type: 'pie', //图形类型
                    radius: ['25%', '75'], //饼图大小 0 - 100
                    center: ['50%', '60%'], //饼图对应整个标签的位置 [X, Y]
                    label: { //饼图图形上的文本标签
                            normal: {
                                show: true, //是否显示文本标签
                                formatter: '{c}', // 文本标签的内容
                            },
                        },
                    data: echarData.data, // 饼图的具体数据
                }
            ]
        };
    } else {
        
        let series = []
        // 定义图形的显示格式
        if(echarData.dataY[0].constructor == Array) {

            console.log(echarData.dataY);
            
            echarData.dataY.map((v, i) => {
                console.log(v);
                series[i] = {}
                series[i].data = v
                series[i].type = echarData.type
                series[i].name = echarData.legendData[i]
            })
        } else {
            series[0] = {}
            series[0].data = echarData.dataY
            series[0].type = echarData.type
        }
        option = {
            title: {
                text: echarData.title,
                x: 'center'
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                x: 'center',
                y: 'bottom',
                data: echarData.legendData
            },
            toolbox: {
                feature: {
                    saveAsImage: {}
                }
            },
            grid: {
                left: '8%',
                right: '4%',
                bottom: '6%',
                containLabel: true
            },
            xAxis: {
                type: 'category',
                data: echarData.dataX,
                // axisLabel: {
                    // interval: 0,// 强制显示所有x值不写会自动隐藏
                    // rotate: 50,  //倾斜50度
                    // fontSize: 11 //字体大小
                // }
            },
            yAxis: {
                type: 'value',
            },
            series: series
        };
    }
    myChart.setOption(option);
};

function exportCSV({tableLable = [], tableData = [], fileUrl = '未命名'}){
    fileUrl += '.csv'
    let addobj = {}
    // 2.1获取表头内容 以rowData形式重新赋值
    try {
        tableLable.map((v, i) => {
            addobj['rowData' + i] = v
        })
    } catch (error) {
        this.$message.error('请填写tableLable表头属性')
        return
    }
    // 2.2用JSON转义清理对象的内存地址关联  来获取表格数据
    let tableData2 = JSON.parse(JSON.stringify(tableData))
    // 2.3把表头添加到表格数据的最前面充当表头
    tableData2.unshift(addobj)
    // 2.4列标题，逗号隔开，每一个逗号就是隔开一个单元格
    let str = ``;
    // 2.5增加\t为了不让表格显示科学计数法或者其他格式
    for(let i = 0; i < tableData2.length; i++) {
        for(let item in tableData2[i]) {
            // 2.5.1 注意要将本身就有换行或者英文逗号的内容进行变换 否则表格内容会错乱
            tableData2[i][item] = tableData2[i][item].replace(/\n/g, ' ')
            tableData2[i][item] = tableData2[i][item].replace(/,/g, '，') // 英文替换为中文
            str += `${tableData2[i][item] + '\t'},`;
        }
        str += '\n';
    }
    // 2.6encodeURIComponent解决中文乱码
    let uri = 'data:text/csv;charset=utf-8,\ufeff' + encodeURIComponent(str);
    // 2.7通过创建a标签实现
    let link = document.createElement('a');
    link.href = uri;
    // 2.8对下载的文件命名
    link.download = fileUrl;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}