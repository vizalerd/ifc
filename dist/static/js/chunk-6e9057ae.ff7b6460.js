(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-6e9057ae"],{2017:function(t,e,n){"use strict";n("cafe")},"23ef":function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{class:t.className,style:{height:t.height,width:t.width},attrs:{id:t.id}})},i=[],s=n("313e"),o=n.n(s),r=n("f42c"),l={mixins:[r["a"]],props:{className:{type:String,default:"chart"},id:{type:String,default:"chart"},width:{type:String,default:"200px"},height:{type:String,default:"200px"}},data:function(){return{chart:null}},mounted:function(){this.initChart()},beforeDestroy:function(){this.chart&&(this.chart.dispose(),this.chart=null)},methods:{initChart:function(){this.chart=o.a.init(document.getElementById(this.id));for(var t=[],e=[],n=[],a=[],i=0;i<50;i++)t.push(i),e.push(5*(Math.sin(i/5)*(i/5-10)+i/6)),n.push(3*(Math.sin(i/5)*(i/5+10)+i/6)),a.push(5*(Math.sin(i/5)*(i/5-10)+i/6)+3*(Math.sin(i/5)*(i/5+10)+i/6));this.chart.setOption({backgroundColor:"#08263a",grid:{left:"5%",right:"5%"},xAxis:[{show:!1,data:t},{show:!1,data:t}],visualMap:{show:!1,min:0,max:50,dimension:0,inRange:{color:["#4a657a","#308e92","#b1cfa5","#f5d69f","#f5898b","#ef5055"]}},yAxis:{axisLine:{show:!1},axisLabel:{textStyle:{color:"#4a657a"}},splitLine:{show:!0,lineStyle:{color:"#08263f"}},axisTick:{show:!1}},series:[,{name:"back",type:"bar",data:n,z:1,itemStyle:{normal:{opacity:.4,barBorderRadius:5,shadowBlur:3,shadowColor:"#111"}}},{name:"Simulate Shadow",type:"line",data:e,z:2,showSymbol:!1,animationDelay:0,animationEasing:"linear",animationDuration:1200,lineStyle:{normal:{color:"transparent"}},areaStyle:{normal:{color:"#08263a",shadowBlur:50,shadowColor:"#000"}}},{name:"front",type:"bar",data:e,xAxisIndex:1,z:3,itemStyle:{normal:{barBorderRadius:5}}}],animationEasing:"elasticOut",animationEasingUpdate:"elasticOut",animationDelay:function(t){return 20*t},animationDelayUpdate:function(t){return 20*t}})}}},c=l,u=n("2877"),d=Object(u["a"])(c,a,i,!1,null,null,null);e["a"]=d.exports},6273:function(t,e,n){"use strict";n("ce4c")},"9ed6":function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"login-container"},[n("el-button",{staticClass:"login_btn",attrs:{type:"success"},on:{click:function(e){t.centerDialogVisible=!0}}},[t._v("Авторизация")]),n("el-dialog",{staticClass:"login_modal",attrs:{title:"",visible:t.centerDialogVisible,width:"70%",center:""},on:{"update:visible":function(e){t.centerDialogVisible=e}}},[n("el-form",{ref:"loginForm",staticClass:"login-form",attrs:{model:t.loginForm,rules:t.loginRules,autocomplete:"off","label-position":"left"}},[n("div",{staticClass:"title-container"},[n("h3",{staticClass:"title"},[t._v(" "+t._s(t.$t("login.title"))+" ")]),n("lang-select",{staticClass:"set-language"})],1),n("el-form-item",{attrs:{prop:"username"}},[n("span",{staticClass:"svg-container"},[n("svg-icon",{attrs:{"icon-class":"user"}})],1),n("el-input",{ref:"username",attrs:{placeholder:t.$t("login.username"),name:"username",type:"text",tabindex:"1",autocomplete:"on"},model:{value:t.loginForm.username,callback:function(e){t.$set(t.loginForm,"username",e)},expression:"loginForm.username"}})],1),n("el-tooltip",{attrs:{content:"Caps lock is On",placement:"right",manual:""},model:{value:t.capsTooltip,callback:function(e){t.capsTooltip=e},expression:"capsTooltip"}},[n("el-form-item",{attrs:{prop:"password"}},[n("span",{staticClass:"svg-container"},[n("svg-icon",{attrs:{"icon-class":"password"}})],1),n("el-input",{key:t.passwordType,ref:"password",attrs:{type:t.passwordType,placeholder:t.$t("login.password"),name:"password",tabindex:"2",autocomplete:"on"},on:{blur:function(e){t.capsTooltip=!1}},nativeOn:{keyup:[function(e){return t.checkCapslock(e)},function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.handleLogin(e)}]},model:{value:t.loginForm.password,callback:function(e){t.$set(t.loginForm,"password",e)},expression:"loginForm.password"}}),n("span",{staticClass:"show-pwd",on:{click:t.showPwd}},[n("svg-icon",{attrs:{"icon-class":"password"===t.passwordType?"eye":"eye-open"}})],1)],1)],1),n("span",{staticStyle:{color:"red"},attrs:{id:"wrong_auth"}}),n("div",{staticStyle:{position:"relative"}},[n("el-button",{staticStyle:{width:"100%","margin-bottom":"30px"},attrs:{type:"primary",loading:t.loading},nativeOn:{click:function(e){return e.preventDefault(),t.handleLogin(t.loginForm.password,t.loginForm.username)}}},[t._v(" "+t._s(t.$t("login.logIn"))+" ")])],1)],1),n("el-dialog",{attrs:{title:t.$t("login.thirdparty"),visible:t.showDialog},on:{"update:visible":function(e){t.showDialog=e}}},[t._v(" "+t._s(t.$t("login.thirdpartyTips"))+" "),n("br"),n("br"),n("br"),n("social-sign")],1)],1),t._m(0),n("div",{staticClass:"chart-container"},[n("chart",{attrs:{height:"100%",width:"100%"}})],1),n("el-row",{staticClass:"main_description"},[n("span",[n("strong",[t._v("InTech-Forecast (iForecast)")]),t._v(" - веб-приложение для прогнозирования выработки электрической энергии объектами ВИЭ")]),n("span",[n("strong",[t._v("Алгоритм работы iForecast:")]),n("br"),n("ul",[n("li",[t._v(" Сбор и анализ исторических метеоданных и объемов производства электроэнергии конкретным объектом ВИЭ ")]),n("li",[t._v(" Создание постоянно обучающегося паттерна (искусственного интеллекта) для обеспечения точных прогнозов объемов производства электроэнергии каждым конкретным объектом ВИЭ на основе прогнозных метеоданных, технического состояния объекта и исторической корреляции метеоданных к объемам выработки электроэнергии ")]),n("li",[t._v(" Автоматическое получение запросов и отправление необходимой информации без участия диспетчера ")])])])])],1)},i=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"logo-conatiner"},[n("img",{attrs:{src:"https://dev.pro100online.kz/logo.svg",alt:""}})])}],s=(n("d3b7"),n("b64b"),n("61f7")),o=n("1131"),r=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"social-signup-container"},[n("div",{staticClass:"sign-btn",on:{click:function(e){return t.wechatHandleClick("wechat")}}},[n("span",{staticClass:"wx-svg-container"},[n("svg-icon",{staticClass:"icon",attrs:{"icon-class":"wechat"}})],1),t._v(" WeChat ")]),n("div",{staticClass:"sign-btn",on:{click:function(e){return t.tencentHandleClick("tencent")}}},[n("span",{staticClass:"qq-svg-container"},[n("svg-icon",{staticClass:"icon",attrs:{"icon-class":"qq"}})],1),t._v(" QQ ")])])},l=[],c={name:"SocialSignin",methods:{wechatHandleClick:function(t){alert("ok")},tencentHandleClick:function(t){alert("ok")}}},u=c,d=(n("d9fb"),n("2877")),p=Object(d["a"])(u,r,l,!1,null,"7309fbbb",null),h=p.exports,g=n("23ef"),f=n("bc3a"),m=n.n(f),w=(n("79e3"),{name:"Login",components:{LangSelect:o["a"],SocialSign:h,Chart:g["a"]},data:function(){var t=function(t,e,n){Object(s["e"])(e)?n():n(new Error("Please enter the correct user name"))},e=function(t,e,n){e.length<6?n(new Error("The password can not be less than 6 digits")):n()};return{centerDialogVisible:!1,loginForm:{username:"",password:""},loginRules:{username:[{required:!0,trigger:"blur",validator:t}],password:[{required:!0,trigger:"blur",validator:e}]},passwordType:"password",capsTooltip:!1,loading:!1,showDialog:!1,redirect:void 0,otherQuery:{},isOK:!1,form:{username:"",password:""}}},watch:{$route:{handler:function(t){var e=t.query;e&&(this.redirect=e.redirect,this.otherQuery=this.getOtherQuery(e))},immediate:!0}},created:function(){},mounted:function(){""===this.loginForm.username?this.$refs.username.focus():""===this.loginForm.password&&this.$refs.password.focus()},destroyed:function(){},methods:{checkCapslock:function(t){var e=t.key;this.capsTooltip=e&&1===e.length&&e>="A"&&e<="Z"},showPwd:function(){var t=this;"password"===this.passwordType?this.passwordType="":this.passwordType="password",this.$nextTick((function(){t.$refs.password.focus()}))},handleLogin:function(t,e){var n=this,a={username:e,password:t},i=this.$appPath+"/login";m.a.post(i,a,{withCredentials:!0}).then((function(t){n.isOK=JSON.parse(t.data.isOK),console.log(n.isOK),"True"==n.isOK?(document.getElementById("wrong_auth").innerHTML="",n.$refs.loginForm.validate((function(t){if(!t)return console.log("error submit!!"),!1;n.loading=!0,n.$store.dispatch("user/login",n.loginForm).then((function(){n.$router.push({path:n.redirect||"/",query:n.otherQuery}),n.loading=!1})).catch((function(){n.loading=!1}))}))):document.getElementById("wrong_auth").innerHTML="Неверный логин или пароль"})).catch((function(t){console.error(t)})).finally((function(){}))},getOtherQuery:function(t){return Object.keys(t).reduce((function(e,n){return"redirect"!==n&&(e[n]=t[n]),e}),{})}}}),b=w,v=(n("2017"),n("6273"),Object(d["a"])(b,a,i,!1,null,"2bdb497e",null));e["default"]=v.exports},a9b3:function(t,e,n){},cafe:function(t,e,n){},ce4c:function(t,e,n){},d9fb:function(t,e,n){"use strict";n("a9b3")}}]);