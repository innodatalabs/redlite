import"../chunks/disclose-version.bJ1TNjgf.js";import{a as x,B as M,r as H,p as h,b as u,u as S,s as p}from"../chunks/runtime.WC_eNKni.js";import{w as T,j as V,n as C,h as q,k as D,m as A,i as j,f as v,g as f,a as w,s as b,d,c as g,o as B,v as z,b as k,e as G}from"../chunks/render.X6cabRiE.js";import{l as E,r as F}from"../chunks/data.UBOtaHlG.js";import{t as I,b as J,f as K,a as N,c as O}from"../chunks/colors.O3kvVj5c.js";import{g as P}from"../chunks/entry.E09qkQD-.js";import{a as _}from"../chunks/load.ybpr34CD.js";var Q=d('<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 w-4 h-4 inline"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 6H5.25A2.25 2.25 0 0 0 3 8.25v10.5A2.25 2.25 0 0 0 5.25 21h10.5A2.25 2.25 0 0 0 18 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25"></path></svg>'),R=d('<div role="presentation"> <!></div>');function U(n,a){x(a,!0);const c=M(a,"format",3,t=>t),i=a.item[a.value||a.label],o=I[a.label];var r=f(n,!0,R);V(r,`p-4 flex items-center ${C(o)}`);var m=w(r),e=b(m);q(r,"title",()=>a.title?a.title(i):void 0),D(m,()=>`${C(c()(i))} `),H(()=>{A(r,"cursor-pointer",!!a.onclick),A(r,"hover:bg-gray-100",!!a.onclick)}),r.__click=function(...t){const l=a.onclick?()=>a.onclick(i):void 0;return l==null?void 0:l.apply(this,t)},j(e,()=>!!a.onclick,t=>{var l=f(t,!0,Q);v(t,l)},null),v(n,r),h()}T(["click"]);var W=d('<div class="p-4"> </div>'),X=d('<div class="grid grid-cols-8 border border-gray-200 rounded-lg m-2"></div>'),Y=d('<div class="grid grid-cols-8 font-bold border border-gray-200 rounded-lg bg-gray-200 m-2"></div> <!>',!0);function Z(n,a){x(a,!0);var s=B(n,!0,Y),c=k(s),i=b(b(c));_(c,()=>a.schema,73,(o,r,m)=>{var e=f(o,!0,W),t=w(e);D(t,()=>u(r).label),v(o,e)},null),_(i,()=>a.data,65,(o,r,m)=>{var e=f(o,!0,X);_(e,()=>a.schema,73,(t,l,ea)=>{var y=G(t),L=k(y);U(L,z({get item(){return u(r)}},()=>u(l))),g(t,y)},null),v(o,e)},null),g(n,s),h()}var $=d("Loading..",!0),aa=d("<div><!></div>");function da(n,a){x(a,!1);const s={};S(s);const c=()=>p(E,"$loading",s),i=()=>p(F,"$runs",s),o=[{label:"run",value:"name",onclick:e=>P(`/run/${e}`)},{label:"model"},{label:"dataset"},{label:"data_digest",format:J,title:e=>e},{label:"metric"},{label:"score_summary",format:K},{label:"completed",format:N},{label:"duration",format:O}];var r=f(n,!0,aa),m=w(r);j(m,c,e=>{var t=B(e,!0,$);g(e,t)},e=>{var t=G(e),l=k(t);Z(l,{schema:o,get data(){return i()}}),g(e,t)}),v(n,r),h()}export{da as component};