(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-230a8364"],{"39f0":function(t,e,a){"use strict";a("b18b")},"48c2":function(t,e,a){"use strict";var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"app-container"},[a("div",{staticClass:"filter-container"}),a("el-table",{key:t.key,staticStyle:{width:"100%"},attrs:{data:t.tableData,border:"",fit:"","highlight-current-row":""}},[a("el-table-column",{attrs:{prop:"name",label:"#",width:"180"}}),t._l(t.formThead,(function(e){return a("el-table-column",{key:e,attrs:{width:"250",label:t.formTheadLabel[e]},scopedSlots:t._u([{key:"default",fn:function(a){return[t._v(" "+t._s(a.row[e])+" ")]}}],null,!0)})}))],2)],1)},s=[],i=(a("4de4"),["apple","banana"]),c={apple:"Дата формирования",banana:"Отчетный период"},r={data:function(){return{tableData:[{name:"1",apple:"24-09-2021",banana:"27-09-2021"},{name:"2",apple:"24-09-2021",banana:"28-09-2021"}],key:1,formTheadOptions:["apple","banana"],checkboxVal:i,formThead:i,formTheadLabel:c}},watch:{checkboxVal:function(t){this.formThead=this.formTheadOptions.filter((function(e){return t.indexOf(e)>=0})),this.key=this.key+1}}},l=r,o=a("2877"),u=Object(o["a"])(l,n,s,!1,null,null,null);e["a"]=u.exports},a9c9:function(t,e,a){},b18b:function(t,e,a){},e5f9:function(t,e,a){"use strict";a("a9c9")},ecac:function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"app-container"},[t.user?a("div",[a("el-row",{attrs:{gutter:20}},[a("el-col",{attrs:{span:6,xs:24}},[a("user-card",{attrs:{user:t.user}})],1),a("el-col",{attrs:{span:18,xs:24}},[a("el-card",[a("el-tabs",{model:{value:t.activeTab,callback:function(e){t.activeTab=e},expression:"activeTab"}},[a("el-tab-pane",{attrs:{label:"Профиль",name:"account"}},[a("account",{attrs:{user:t.user}})],1),a("el-tab-pane",{attrs:{label:"Настройки",name:"account_settings"}},[a("activity",{attrs:{user:t.user}})],1)],1)],1)],1)],1)],1):t._e()])},s=[],i=a("5530"),c=(a("b0c0"),a("a15b"),a("2f62")),r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-card",{staticStyle:{"margin-bottom":"20px"}},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("span",[t._v("Профиль")])]),a("div",{staticClass:"user-profile"},[a("div",{staticClass:"box-center"},[a("img",{staticStyle:{width:"100% !important"},attrs:{src:"https://care-tech.kz/logo.svg",alt:""}})]),a("div",{staticClass:"box-center"},[a("div",{staticClass:"user-name text-center"},[t._v("Modern Innovative Technologies")]),a("div",{staticClass:"user-role text-center text-muted"},[t._v("Жаксылык Ануар")])])])])},l=[],o=a("3cbc"),u={components:{PanThumb:o["a"]},props:{user:{type:Object,default:function(){return{name:"",email:"",avatar:"",role:""}}}}},p=u,m=(a("e5f9"),a("2877")),_=Object(m["a"])(p,r,l,!1,null,"3461e780",null),d=_.exports,f=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"block account_settings_wrapper"},[a("div",{staticClass:"block account_settings"},[a("h3",[t._v("Общие настройки")]),a("div",{staticClass:"settings_item"},[a("span",[t._v("Общая выработка")]),a("el-switch",{model:{value:t.account_setting_1,callback:function(e){t.account_setting_1=e},expression:"account_setting_1"}})],1),a("div",{staticClass:"settings_item"},[a("span",[t._v("КИУМ")]),a("el-switch",{model:{value:t.account_setting_2,callback:function(e){t.account_setting_2=e},expression:"account_setting_2"}})],1),a("div",{staticClass:"settings_item"},[a("span",[t._v("Техническая готовность")]),a("el-switch",{model:{value:t.account_setting_3,callback:function(e){t.account_setting_3=e},expression:"account_setting_3"}})],1),a("div",{staticClass:"settings_item"},[a("span",[t._v("Метеоданные")]),a("el-switch",{model:{value:t.account_setting_4,callback:function(e){t.account_setting_4=e},expression:"account_setting_4"}})],1),a("div",{staticClass:"settings_item"},[a("span",[t._v("Суточная выработка")]),a("el-switch",{model:{value:t.account_setting_5,callback:function(e){t.account_setting_5=e},expression:"account_setting_5"}})],1),a("div",{staticClass:"settings_item"},[a("span",[t._v("Доход")]),a("el-switch",{model:{value:t.account_setting_6,callback:function(e){t.account_setting_6=e},expression:"account_setting_6"}})],1),a("div",{staticClass:"settings_item"},[a("span",[t._v("Снижение выбросов")]),a("el-switch",{model:{value:t.account_setting_7,callback:function(e){t.account_setting_7=e},expression:"account_setting_7"}})],1)]),a("br"),a("br"),a("br"),a("h3",[t._v("Планировщик")]),a("h4",[t._v("Запланированные задачи")]),a("div",{staticClass:"task-wrapper"},[a("table",{staticClass:"report_table"},[t._m(0),t._l(t.report_id,(function(e){return a("tr",{key:e.id},[a("th",[t._v(" "+t._s(t.report_id[e])+" ")]),a("td",[t._v(" "+t._s(t.report_date[e])+" ")]),a("td",[t._v(" "+t._s(t.report_target[e])+" ")])])}))],2)]),a("h4",[t._v("Добавить новую")]),a("br"),a("el-col",{staticClass:"date-panel-group",attrs:{xs:24,sm:24,lg:24}},[a("span",{staticClass:"demonstration"},[t._v("Выберите дату:")]),a("br"),a("el-date-picker",{attrs:{type:"datetime",placeholder:"Дата отчета"},on:{change:function(e){return t.handleDate2(t.value2)}},model:{value:t.value2,callback:function(e){t.value2=e},expression:"value2"}}),a("button",{staticClass:"el-button el-button--primary el-button--medium",on:{click:t.postReport}},[t._v("Добавить")])],1)],1)},h=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("tr",[a("th",[t._v("ID")]),a("th",[t._v("Дата формирования")]),a("th",[t._v("Отчетный период")])])}],v=(a("d3b7"),a("48c2")),b=a("bc3a"),g=a.n(b),k={name:"DynamicTable",components:{FixedThead:v["a"]},data:function(){return{account_setting_1:!0,account_setting_2:!0,account_setting_3:!0,account_setting_4:!0,account_setting_5:!0,account_setting_6:!0,account_setting_7:!0,report_id:[],report_date:[],report_target:[],report_new:(new Date).getTime(),pickerOptions:{shortcuts:[{text:"Неделя",onClick:function(t){var e=new Date,a=new Date;a.setTime(a.getTime()-6048e5),t.$emit("pick",[a,e])}},{text:"Месяц",onClick:function(t){var e=new Date,a=new Date;a.setTime(a.getTime()-2592e6),t.$emit("pick",[a,e])}},{text:"3 месяца",onClick:function(t){var e=new Date,a=new Date;a.setTime(a.getTime()-7776e6),t.$emit("pick",[a,e])}}]},value2:(new Date).getTime()}},methods:{getReports:function(){var t=this,e=this.$appPath+"/getreports";g.a.get(e,{withCredentials:!0}).then((function(e){t.report_id=JSON.parse(e.data.report_id),t.report_date=JSON.parse(e.data.report_date),t.report_target=JSON.parse(e.data.report_target)})).catch((function(t){console.error(t)})).finally((function(){}))},handleDate2:function(t){this.report_new=t},postReport:function(){var t=this,e=this.$appPath+"/postreports";g.a.post(e,this.report_new,{withCredentials:!0}).then((function(e){t.getReports()})).catch((function(t){console.error(t)})).finally((function(){t.$forceUpdate()}))}},mounted:function(){this.getReports()}},w=k,x=(a("39f0"),Object(m["a"])(w,f,h,!1,null,"0439470c",null)),C=x.exports,y=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"block"},[a("el-timeline",t._l(t.timeline,(function(e,n){return a("el-timeline-item",{key:n,attrs:{timestamp:e.timestamp,placement:"top"}},[a("el-card",[a("h4",[t._v(t._s(e.title))]),a("p",[t._v(t._s(e.content))])])],1)})),1)],1)},T=[],O={data:function(){return{timeline:[{timestamp:"2019/4/20",title:"Update Github template",content:"PanJiaChen committed 2019/4/20 20:46"},{timestamp:"2019/4/21",title:"Update Github template",content:"PanJiaChen committed 2019/4/21 20:46"},{timestamp:"2019/4/22",title:"Build Template",content:"PanJiaChen committed 2019/4/22 20:46"},{timestamp:"2019/4/23",title:"Release New Version",content:"PanJiaChen committed 2019/4/23 20:46"}]}}},$=O,D=Object(m["a"])($,y,T,!1,null,null,null),j=D.exports,J=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-form",[a("el-form-item",{attrs:{label:"Станция"}},[a("br"),a("span",[t._v("Кенгир 10МВт Казахстан")])]),a("el-form-item",{attrs:{label:"Логин"}},[a("br"),a("span",[t._v("admin")])]),a("el-form-item",{attrs:{label:"Пароль"}},[a("el-input")],1),a("el-form-item",{attrs:{label:"Email"}},[a("el-input",{model:{value:t.user.email,callback:function(e){t.$set(t.user,"email","string"===typeof e?e.trim():e)},expression:"user.email"}})],1),a("el-form-item",{attrs:{label:"Телефон"}},[a("el-input",{model:{value:t.user.phone,callback:function(e){t.$set(t.user,"phone","string"===typeof e?e.trim():e)},expression:"user.phone"}})],1),a("el-form-item",[a("el-button",{attrs:{type:"primary"},on:{click:t.submit}},[t._v("Обновить")])],1)],1)},E=[],P={props:{user:{type:Object,default:function(){return{name:"",email:""}}}},methods:{submit:function(){this.$message({message:"User information has been updated successfully",type:"success",duration:5e3})}}},S=P,U=Object(m["a"])(S,J,E,!1,null,null,null),R=U.exports,N={name:"Profile",components:{UserCard:d,Activity:C,Timeline:j,Account:R},data:function(){return{user:{},activeTab:"account"}},computed:Object(i["a"])({},Object(c["b"])(["name","avatar","roles"])),created:function(){this.getUser()},methods:{getUser:function(){this.user={name:this.name,role:this.roles.join(" | "),email:"admin@test.com",avatar:this.avatar}}}},V=N,A=Object(m["a"])(V,n,s,!1,null,null,null);e["default"]=A.exports}}]);