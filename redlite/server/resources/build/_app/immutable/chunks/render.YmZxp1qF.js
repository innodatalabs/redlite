import{C as D,f as R,i as C,e as S,D as q,F as he,G as N,A as B,g as P,U as x,H as W,I as ge,J as F,K as me,j as w,L as ye,M as be,r as m,h as I,N as xe,v as L,O as ve,P as X,Q as we,R as ke,a as Ne,S as Ee,p as Se,T as Le,V as ee,W as Te,X as Ae,Y as te,Z as Ce,_ as Y,$ as G,a0 as Oe,a1 as Pe,a2 as $e,a3 as $}from"./runtime.WC_eNKni.js";const v=Symbol("$state"),je=Object.prototype,ze=Array.prototype,De=Object.getPrototypeOf,Re=Object.isFrozen;function A(e,t=!0){if(typeof e=="object"&&e!=null&&!Re(e)){if(v in e)return e[v].p;const n=De(e);if(n===je||n===ze){const s=new Proxy(e,Ie);return D(e,v,{value:Me(e,s,t),writable:!1}),s}}return e}function Me(e,t,n){return{s:new Map,v:R(0),a:C(e),i:n,p:t}}const Ie={defineProperty(e,t,n){if(n.value){const s=e[v],l=s.s.get(t);l!==void 0&&S(l,A(n.value,s.i))}return Reflect.defineProperty(e,t,n)},deleteProperty(e,t){const n=e[v],s=n.s.get(t),l=n.a,i=delete e[t];if(l&&i){const r=n.s.get("length"),d=e.length-1;r!==void 0&&r.v!==d&&S(r,d)}return s!==void 0&&S(s,x),t in e&&q(n.v),i},get(e,t,n){var i;const s=e[v];let l=s.s.get(t);if(l===void 0&&(W()||he)&&(!(t in e)||(i=N(e,t))!=null&&i.writable)&&(l=(s.i?R:B)(A(e[t],s.i)),s.s.set(t,l)),l!==void 0){const r=P(l);return r===x?void 0:r}return Reflect.get(e,t,n)},getOwnPropertyDescriptor(e,t){const n=Reflect.getOwnPropertyDescriptor(e,t);if(n&&"value"in n){const l=e[v].s.get(t);l&&(n.value=P(l))}return n},has(e,t){var i;if(t===v)return!0;const n=e[v],s=Reflect.has(e,t);let l=n.s.get(t);return(l!==void 0||W()&&(!s||(i=N(e,t))!=null&&i.writable))&&(l===void 0&&(l=(n.i?R:B)(s?A(e[t],n.i):x),n.s.set(t,l)),P(l)===x)?!1:s},set(e,t,n){const s=e[v],l=s.s.get(t);l!==void 0&&S(l,A(n,s.i));const i=s.a,r=!(t in e);if(i&&t==="length")for(let d=n;d<e.length;d+=1){const c=s.s.get(d+"");c!==void 0&&S(c,x)}if(r&&q(s.v),e[t]=n,i&&r){const d=s.s.get("length"),c=e.length;d!==void 0&&d.v!==c&&S(d,c)}return!0},ownKeys(e){const t=e[v];return P(t.v),Reflect.ownKeys(e)}};let g=null;function E(e){g=e}function V(e){const t=[];let n=e,s=null;for(;n!==null;){const l=n.nodeType,i=n.nextSibling;if(l===8){const r=n.data;if(r.startsWith("ssr:")){const d=r.slice(4);if(s===null)s=d;else{if(d===s)return t;t.push(n)}n=i;continue}}s!==null&&t.push(n),n=i}return null}function O(e,t){let n=e;if(g!==null)if(t&&(n=n.firstChild),n.nodeType===8){let s=n.$$fragment;s===void 0?s=V(n):ge(()=>{n.$$fragment=void 0}),E(s)}else{const s=n.firstChild;E(s===null?[]:[s])}}var k,j,J,z,ne,se,le,ie,K,re,oe,ce;function Ve(){k===void 0&&(k=Node.prototype,j=Element.prototype,J=Text.prototype,z=Map.prototype,ne=k.appendChild,se=k.cloneNode,le=z.set,ie=z.get,z.delete,j.__click=void 0,J.__nodeValue=" ",j.__className="",K=N(k,"firstChild").get,re=N(k,"nextSibling").get,oe=N(k,"textContent").set,ce=N(j,"className").set)}function U(e,t){ne.call(e,t)}function Ke(e,t,n){le.call(e,t,n)}function He(e,t){return ie.call(e,t)}function qe(e,t){return se.call(e,t)}function Be(e){const t=K.call(e);if(g!==null)if(t===null){const n=document.createTextNode("");return e.appendChild(n),n}else return H(t);return t}function ut(e){if(g!==null){const t=e[0];return g!==null&&t!==null?H(t):t}return K.call(e)}function dt(e){const t=re.call(e);return g!==null&&t!==null?H(t):t}function We(e,t){ce.call(e,t)}function _t(e){oe.call(e,"")}function H(e){if(e.nodeType===8&&e.data.startsWith("ssr:")&&g.at(-1)!==e){const t=V(e),s=(t.at(-1)||e).nextSibling;return s.$$fragment=t,s}return e}function Fe(e){var t=document.createElement("template");return t.innerHTML=e,t.content}function Ye(e,t,n){if(C(e)){for(var s=0,l;s<e.length;s++)l=e[s],n===null?U(t,l):n.before(l);return e[0]}else e!==null&&(n===null?U(t,e):n.before(e));return e}function y(e){var t=e;if(C(e))for(var n=0,s;n<e.length;n++)s=e[n],n===0&&(t=s),s.isConnected&&s.remove();else e.isConnected&&e.remove();return t}function T(e,t,n){const s=[];for(const l of e){const i=l.r,r=l.e;t==="in"?(i==="in"||i==="both"?l.in():l.c(),l.d.inert=!1,F(r,r,!1)):t==="key"?i==="key"&&(l.p=l.i(n),l.in()):((i==="out"||i==="both")&&(l.p=l.i(),s.push(l.o)),l.d.inert=!0,F(r,r,!0))}if(s.length>0){const l=me(()=>{w(l);const i=ye(()=>{w(i),be(s)})},!1)}}const fe=new Set,M=new Set;function Ge(){return document.createTextNode("")}function ae(e,t){let n;return()=>{if(n===void 0){const s=Fe(e);n=t?s:Be(s)}return n}}function ue(e,t,n,s){if(g!==null){n!==null&&O(n,!1);const l=g;if(l!==null)return e?l:l[0]}return t?qe(s(),!0):document.importNode(s(),!0)}function Je(e,t,n){return ue(!1,t,e,n)}function Ue(e,t,n){return ue(!0,t,e,n)}const Ze=ae(" ",!1),Qe=ae("<!>",!0);function pt(e){return Je(e,!0,Ze)}function ht(e){return Ue(e,!0,Qe)}function de(e,t,n){const s=ee,l=t?C(e)?e:Array.from(e.childNodes):e;n!==null&&g===null&&Ye(l,null,n),s.d=l}function gt(e,t){de(t,!1,e)}function mt(e,t){de(t,!0,e)}function yt(e,t,n,s,l){const i={capture:s,passive:l},r=n;t.addEventListener(e,r,i),(t===document.body||t===window||t===document)&&m(()=>()=>{t.removeEventListener(e,r,i)})}function bt(e,t){const n=e.__className,s=tt(t),l=g!==null;l&&e.className===s?e.__className=s:(n!==s||l&&e.className!==s)&&(s===""?e.removeAttribute("class"):We(e,s),e.__className=s)}function xt(e,t){m(()=>Xe(e,t()))}function Xe(e,t){const n=e.__nodeValue,s=lt(t);g!==null&&e.nodeValue===s?e.__nodeValue=s:n!==s&&(e.nodeValue=s,e.__nodeValue=s)}function et(e,t){if(t){const n=document.body;e.autofocus=!0,m(()=>{document.activeElement===n&&e.focus()},ee,!0,!1)}}function tt(e){return e??""}function nt(e,t,n){n?e.classList.add(t):e.classList.remove(t)}function vt(e,t,n){m(()=>{const s=n();nt(e,t,s)})}function wt(e,t,n){G(()=>{t(e),m(()=>()=>{m(()=>{G(()=>{(!Oe(n)||n.v===e)&&t(null)})})})})}function st(e){for(let t=0;t<e.length;t++)fe.add(e[t]);for(const t of M)t(e)}function Z(e,t){var d;const n=t.type,s=((d=t.composedPath)==null?void 0:d.call(t))||[];let l=s[0]||t.target;t.target!==l&&D(t,"target",{configurable:!0,value:l});let i=0;const r=t.__root;if(r){const c=s.indexOf(r);if(c!==-1&&e===document)return;c<s.indexOf(e)&&(i=c)}for(l=s[i]||t.target,D(t,"currentTarget",{configurable:!0,get(){return l||document}});l!==null;){const c=l.parentNode||l.host||null,o="__"+n,_=l[o];if(_!==void 0&&!l.disabled)if(C(_)){const[f,...p]=_;f.apply(l,[t,...p])}else _.call(l,t);if(t.cancelBubble||c===e)break;l=c}t.__root=e}function kt(e,t,n,s){O(e),t===void 0?s!==null&&s(e):t(e,n)}function Nt(e,t,n,s){const l=xe();O(e);const i=g;let r=null,d=null,c=!1,o=!1;const _=m(()=>{var a;const b=!!t();if(l.v!==b||!c){if(l.v=b,c){const u=l.c,h=l.a;b?(h===null||h.size===0?L(p):T(h,"out"),u===null||u.size===0?L(f):T(u,"in")):(u===null||u.size===0?L(f):T(u,"out"),h===null||h.size===0?L(p):T(h,"in"))}else if(g!==null){const u=(a=g==null?void 0:g[0])==null?void 0:a.data;!u||u==="ssr:if:true"&&!b||u==="ssr:if:false"&&b?(y(g),E(null)):g.shift()}c=!0}},l,!1),f=m(()=>{r!==null&&(y(r),r=null),l.v&&(n(e),o||(E(i),o=!0)),r=l.d,l.d=null},l,!0);l.ce=f;const p=m(()=>{d!==null&&(y(d),d=null),l.v||(s!==null&&s(e),o||(E(i),o=!0)),d=l.d,l.d=null},l,!0);l.ae=p,I(_,()=>{r!==null&&y(r),d!==null&&y(d),w(f),w(p)}),l.e=_}function Et(e,t,n){const s=Te();let l=null;O(e);let i=null;s.r=o=>{const _=l,f=_.s;f.add(o),o.f(()=>{f.delete(o),f.size===0&&_.e!==null&&(_.d!==null&&(y(_.d),_.d=null),w(_.e),_.e=null)})};const r=()=>{const o={d:null,e:null,s:new Set,p:l},_=m(()=>{const f=s.d;f!==null&&(y(f),s.d=null),i&&n(i),o.d=s.d,s.d=null},s,!0);o.e=_,l=o},d=()=>{const o=l;if(o===null){r();return}const _=o.s;_.size===0?(o.d!==null&&(y(o.d),o.d=null),o.e?L(o.e):r()):(r(),T(_,"out"))},c=m(()=>{const o=t();i!==o&&(i=o,d())},s,!1);I(c,()=>{let o=l;for(;o!==null;){const _=o.d;_!==null&&y(_);const f=o.e;f!==null&&w(f),o=o.p}}),s.e=c}function St(e,t,n,s,l){const i=Ae();let r=null;O(e);let d,c=x,o=x,_=!1;i.r=a=>{const u=r,h=u.s;h.add(a),a.f(()=>{h.delete(a),h.size===0&&u.e!==null&&(u.d!==null&&(y(u.d),u.d=null),w(u.e),u.e=null)})};const f=()=>{const a={d:null,e:null,s:new Set,p:r},u=m(()=>{o===x?c===x?(i.n=!0,n!==null&&n(e)):s!==null&&(i.n=!1,s(e,c)):l!==null&&(i.n=!1,l(e,o)),a.d=i.d,i.d=null},i,!0,!0);a.e=u,r=a},p=()=>{const a=r;if(a===null){f();return}const u=a.s;u.size===0?(a.d!==null&&(y(a.d),a.d=null),a.e?L(a.e):f()):(f(),T(u,"out"))},b=m(()=>{const a={};d=a;const u=t();ve(u)?(u.then(h=>{d===a&&(X(),c=h,_=!1,p())},h=>{o=h,_=!1,p()}),(c!==x||o!==x)&&(o=x,c=x),_||(_=!0,p())):(o=x,c=u,_=!1,p())},i,!1);I(b,()=>{let a=r;for(d={};a!==null;){const u=a.d;u!==null&&y(u);const h=a.e;h!==null&&w(h),a=a.p}}),i.e=b}function lt(e){return typeof e=="string"?e:e==null?"":e+""}function Lt(e,t,n){m(()=>{const s=n();_e(e,t,s)})}function _e(e,t,n){n=n==null?null:n+"",(g===null||e.getAttribute(t)!==n&&t!=="src"&&t!=="href"&&t!=="srcset")&&(n===null?e.removeAttribute(t):e.setAttribute(t,n))}const it=["width","height"],Q=new Map;function rt(e){const t=[],n=Pe(e.__proto__);for(const s in n)n[s].set&&!it.includes(s)&&t.push(s);return t}function Tt(e,t,n,s){let l;m(()=>{l=ot(e,l,t(),n,s)})}function ot(e,t,n,s,l){const i=te({},...n),r=l.length!==0;for(const c in t)c in i||(i[c]=null);r&&!i.class&&(i.class="");let d=He(Q,e.nodeName);d||Ke(Q,e.nodeName,d=rt(e));for(const c in i){let o=i[c];if(o===(t==null?void 0:t[c]))continue;const _=c[0]+c[1];if(_!=="$$")if(_==="on"){const f={};let p=c.slice(2);const b=$e.includes(p);p.endsWith("capture")&&p!=="ongotpointercapture"&&p!=="onlostpointercapture"&&(p=p.slice(0,-7),f.capture=!0),!b&&(t!=null&&t[c])&&e.removeEventListener(p,t[c],f),o!=null&&(b?(e[`__${p}`]=o,st([p])):e.addEventListener(p,o,f))}else if(o==null)e.removeAttribute(c);else if(c==="style")e.style.cssText=o+"";else if(c==="autofocus")et(e,!!o);else if(c==="__value"||c==="value")e.value=e[c]=e.__value=o;else{let f=c;s&&(f=f.toLowerCase(),f=Ce[f]||f),d.includes(f)?(g===null||e[f]!==o&&f!=="src"&&f!=="href"&&f!=="srcset")&&(e[f]=o):typeof o!="function"&&(r&&f==="class"&&(o&&(o+=" "),o+=l),_e(e,f,o))}}return i}const ct={get(e,t){if(!e.exclude.includes(t))return e.props[t]},getOwnPropertyDescriptor(e,t){if(!e.exclude.includes(t)&&t in e.props)return{enumerable:!0,configurable:!0,value:e.props[t]}},has(e,t){return e.exclude.includes(t)?!1:t in e.props},ownKeys(e){const t=[];for(let n in e.props)e.exclude.includes(n)||t.push(n);return t}};function At(e,t){return new Proxy({props:e,exclude:t},ct)}const ft={get(e,t){let n=e.props.length;for(;n--;){let s=e.props[n];if($(s)&&(s=s()),typeof s=="object"&&s!==null&&t in s)return s[t]}},getOwnPropertyDescriptor(e,t){let n=e.props.length;for(;n--;){let s=e.props[n];if($(s)&&(s=s()),typeof s=="object"&&s!==null&&t in s)return N(s,t)}},has(e,t){for(let n of e.props)if($(n)&&(n=n()),t in n)return!0;return!1},ownKeys(e){const t=[];for(let n of e.props){$(n)&&(n=n());for(const s in n)t.includes(s)||t.push(s)}return t}};function Ct(...e){return new Proxy({props:e},ft)}function Ot(e,t){const n=A(t.props||{},!1);let[s,l]=pe(e,{...t,props:n});const i={$set:r=>{te(n,r)},$destroy:l};for(const r of we(s||{}))D(i,r,{get(){return s[r]},set(d){X(()=>s[r]=d)},enumerable:!0});return i}function pe(e,t){var p,b;Ve();const n=new Set,s=t.target,l=ke(t.intro||!1),i=s.firstChild,r=V(i),d=g;let c;try{let a=null;r===null&&(a=Ge(),s.appendChild(a)),E(r);const u=m(()=>{t.context&&(Ne({}),Ee.c=t.context),c=e(a,t.props||{}),t.context&&Se()},l,!0);l.e=u}catch(a){if(t.recover!==!1&&r!==null)return console.error("ERR_SVELTE_HYDRATION_MISMATCH",a),y(r),i.remove(),(b=(p=r.at(-1))==null?void 0:p.nextSibling)==null||b.remove(),pe(e,t);throw a}finally{E(d)}const o=Z.bind(null,s),_=Z.bind(null,document),f=a=>{for(let u=0;u<a.length;u++){const h=a[u];n.has(h)||(n.add(h),s.addEventListener(h,o,Y.includes(h)?{passive:!0}:void 0),document.addEventListener(h,_,Y.includes(h)?{passive:!0}:void 0))}};return f(Le(fe)),M.add(f),[c,()=>{for(const u of n)s.removeEventListener(u,o);M.delete(f);const a=l.d;a!==null&&y(a),r!==null&&y(r),w(l.e)}]}export{y as A,T as B,_t as C,g as D,V as E,E as F,Ke as G,He as H,Ye as I,Ge as J,Tt as K,A as L,yt as M,Ot as N,Et as O,v as S,Be as a,ut as b,mt as c,ae as d,ht as e,gt as f,Je as g,Lt as h,Nt as i,bt as j,ot as k,nt as l,lt as m,wt as n,Ue as o,xt as p,pt as q,At as r,dt as s,Xe as t,St as u,Ct as v,st as w,kt as x,vt as y,O as z};
