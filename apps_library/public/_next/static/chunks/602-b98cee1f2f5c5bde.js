(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[602],{3725:function(e,r,t){"use strict";t.d(r,{x:function(){return u}});var l=t(7294),o=t(3967),n=t.n(o),a=t(8426);let i={display:{type:"enum",values:["none","inline","inline-block","block"],default:void 0,responsive:!0}};var c=t(3843),s=t(134),d=t(6776);let u=l.forwardRef((e,r)=>{let{rest:t,...o}=(0,c.FY)(e),{rest:u,...f}=(0,s.F8)(t),{className:h,asChild:v,display:p=i.display.default,...b}=u,m=v?a.g7:"div";return l.createElement(m,{...b,ref:r,className:n()("rt-Box",h,(0,d.g)(p,"rt-r-display"),(0,s.yt)(f),(0,c.we)(o))})});u.displayName="Box"},4152:function(e,r,t){"use strict";t.d(r,{z:function(){return v}});var l=t(7294),o=t(3967),n=t.n(o),a=t(8426),i=t(8291),c=t(6679),s=t(8219);let d={size:{type:"enum",values:["1","2","3","4"],default:"2",responsive:!0},variant:{type:"enum",values:["classic","solid","soft","surface","outline","ghost"],default:"solid"},color:i.m,highContrast:c.B,radius:s.C};var u=t(3843),f=t(6776);let h=l.forwardRef((e,r)=>{let{rest:t,...o}=(0,u.FY)(e),{className:i,asChild:c=!1,size:s=d.size.default,variant:h=d.variant.default,color:v=d.color.default,highContrast:p=d.highContrast.default,radius:b=d.radius.default,...m}=t,w=c?a.g7:"button";return l.createElement(w,{"data-disabled":m.disabled||void 0,"data-accent-color":v,"data-radius":b,...m,ref:r,className:n()("rt-reset","rt-BaseButton",i,(0,f.g)(s,"rt-r-size"),`rt-variant-${h}`,{"rt-high-contrast":p},(0,u.we)(o))})});h.displayName="BaseButton";let v=l.forwardRef((e,r)=>l.createElement(h,{...e,ref:r,className:n()("rt-Button",e.className)}));v.displayName="Button"},9248:function(e,r,t){"use strict";t.d(r,{x:function(){return F}});var l=t(7294),o=t(3967),n=t.n(o),a=t(7462),i=t(5320),c=t(9115),s=t(5360),d=t(8771),u=t(9698),f=t(8990),h=t(9981);function $ae6933e535247d3d$export$7d15b64cf5a3a4c4(e,[r,t]){return Math.min(t,Math.max(r,e))}var v=t(6206);function $6c2e24571c90391f$export$3e6543de14f8614f(e,r){return(0,l.useReducer)((e,t)=>{let l=r[e][t];return null!=l?l:e},e)}let p="ScrollArea",[b,m]=(0,s.b)(p),[w,g]=b(p),$=(0,l.forwardRef)((e,r)=>{let{__scopeScrollArea:t,type:o="hover",dir:n,scrollHideDelay:c=600,...s}=e,[u,h]=(0,l.useState)(null),[v,p]=(0,l.useState)(null),[b,m]=(0,l.useState)(null),[g,$]=(0,l.useState)(null),[S,E]=(0,l.useState)(null),[y,T]=(0,l.useState)(0),[C,R]=(0,l.useState)(0),[P,z]=(0,l.useState)(!1),[D,L]=(0,l.useState)(!1),_=(0,d.e)(r,e=>h(e)),A=(0,f.gm)(n);return(0,l.createElement)(w,{scope:t,type:o,dir:A,scrollHideDelay:c,scrollArea:u,viewport:v,onViewportChange:p,content:b,onContentChange:m,scrollbarX:g,onScrollbarXChange:$,scrollbarXEnabled:P,onScrollbarXEnabledChange:z,scrollbarY:S,onScrollbarYChange:E,scrollbarYEnabled:D,onScrollbarYEnabledChange:L,onCornerWidthChange:T,onCornerHeightChange:R},(0,l.createElement)(i.WV.div,(0,a.Z)({dir:A},s,{ref:_,style:{position:"relative","--radix-scroll-area-corner-width":y+"px","--radix-scroll-area-corner-height":C+"px",...e.style}})))}),S=(0,l.forwardRef)((e,r)=>{let{__scopeScrollArea:t,children:o,...n}=e,c=g("ScrollAreaViewport",t),s=(0,l.useRef)(null),u=(0,d.e)(r,s,c.onViewportChange);return(0,l.createElement)(l.Fragment,null,(0,l.createElement)("style",{dangerouslySetInnerHTML:{__html:"[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}"}}),(0,l.createElement)(i.WV.div,(0,a.Z)({"data-radix-scroll-area-viewport":""},n,{ref:u,style:{overflowX:c.scrollbarXEnabled?"scroll":"hidden",overflowY:c.scrollbarYEnabled?"scroll":"hidden",...e.style}}),(0,l.createElement)("div",{ref:c.onContentChange,style:{minWidth:"100%",display:"table"}},o)))}),E="ScrollAreaScrollbar",y=(0,l.forwardRef)((e,r)=>{let{forceMount:t,...o}=e,n=g(E,e.__scopeScrollArea),{onScrollbarXEnabledChange:i,onScrollbarYEnabledChange:c}=n,s="horizontal"===e.orientation;return(0,l.useEffect)(()=>(s?i(!0):c(!0),()=>{s?i(!1):c(!1)}),[s,i,c]),"hover"===n.type?(0,l.createElement)(T,(0,a.Z)({},o,{ref:r,forceMount:t})):"scroll"===n.type?(0,l.createElement)(C,(0,a.Z)({},o,{ref:r,forceMount:t})):"auto"===n.type?(0,l.createElement)(R,(0,a.Z)({},o,{ref:r,forceMount:t})):"always"===n.type?(0,l.createElement)(P,(0,a.Z)({},o,{ref:r})):null}),T=(0,l.forwardRef)((e,r)=>{let{forceMount:t,...o}=e,n=g(E,e.__scopeScrollArea),[i,s]=(0,l.useState)(!1);return(0,l.useEffect)(()=>{let e=n.scrollArea,r=0;if(e){let handlePointerEnter=()=>{window.clearTimeout(r),s(!0)},handlePointerLeave=()=>{r=window.setTimeout(()=>s(!1),n.scrollHideDelay)};return e.addEventListener("pointerenter",handlePointerEnter),e.addEventListener("pointerleave",handlePointerLeave),()=>{window.clearTimeout(r),e.removeEventListener("pointerenter",handlePointerEnter),e.removeEventListener("pointerleave",handlePointerLeave)}}},[n.scrollArea,n.scrollHideDelay]),(0,l.createElement)(c.z,{present:t||i},(0,l.createElement)(R,(0,a.Z)({"data-state":i?"visible":"hidden"},o,{ref:r})))}),C=(0,l.forwardRef)((e,r)=>{let{forceMount:t,...o}=e,n=g(E,e.__scopeScrollArea),i="horizontal"===e.orientation,s=$57acba87d6e25586$var$useDebounceCallback(()=>u("SCROLL_END"),100),[d,u]=$6c2e24571c90391f$export$3e6543de14f8614f("hidden",{hidden:{SCROLL:"scrolling"},scrolling:{SCROLL_END:"idle",POINTER_ENTER:"interacting"},interacting:{SCROLL:"interacting",POINTER_LEAVE:"idle"},idle:{HIDE:"hidden",SCROLL:"scrolling",POINTER_ENTER:"interacting"}});return(0,l.useEffect)(()=>{if("idle"===d){let e=window.setTimeout(()=>u("HIDE"),n.scrollHideDelay);return()=>window.clearTimeout(e)}},[d,n.scrollHideDelay,u]),(0,l.useEffect)(()=>{let e=n.viewport,r=i?"scrollLeft":"scrollTop";if(e){let t=e[r],handleScroll=()=>{let l=e[r],o=t!==l;o&&(u("SCROLL"),s()),t=l};return e.addEventListener("scroll",handleScroll),()=>e.removeEventListener("scroll",handleScroll)}},[n.viewport,i,u,s]),(0,l.createElement)(c.z,{present:t||"hidden"!==d},(0,l.createElement)(P,(0,a.Z)({"data-state":"hidden"===d?"hidden":"visible"},o,{ref:r,onPointerEnter:(0,v.M)(e.onPointerEnter,()=>u("POINTER_ENTER")),onPointerLeave:(0,v.M)(e.onPointerLeave,()=>u("POINTER_LEAVE"))})))}),R=(0,l.forwardRef)((e,r)=>{let t=g(E,e.__scopeScrollArea),{forceMount:o,...n}=e,[i,s]=(0,l.useState)(!1),d="horizontal"===e.orientation,u=$57acba87d6e25586$var$useDebounceCallback(()=>{if(t.viewport){let e=t.viewport.offsetWidth<t.viewport.scrollWidth,r=t.viewport.offsetHeight<t.viewport.scrollHeight;s(d?e:r)}},10);return $57acba87d6e25586$var$useResizeObserver(t.viewport,u),$57acba87d6e25586$var$useResizeObserver(t.content,u),(0,l.createElement)(c.z,{present:o||i},(0,l.createElement)(P,(0,a.Z)({"data-state":i?"visible":"hidden"},n,{ref:r})))}),P=(0,l.forwardRef)((e,r)=>{let{orientation:t="vertical",...o}=e,n=g(E,e.__scopeScrollArea),i=(0,l.useRef)(null),c=(0,l.useRef)(0),[s,d]=(0,l.useState)({content:0,viewport:0,scrollbar:{size:0,paddingStart:0,paddingEnd:0}}),u=$57acba87d6e25586$var$getThumbRatio(s.viewport,s.content),f={...o,sizes:s,onSizesChange:d,hasThumb:!!(u>0&&u<1),onThumbChange:e=>i.current=e,onThumbPointerUp:()=>c.current=0,onThumbPointerDown:e=>c.current=e};function getScrollPosition(e,r){return $57acba87d6e25586$var$getScrollPositionFromPointer(e,c.current,s,r)}return"horizontal"===t?(0,l.createElement)(z,(0,a.Z)({},f,{ref:r,onThumbPositionChange:()=>{if(n.viewport&&i.current){let e=n.viewport.scrollLeft,r=$57acba87d6e25586$var$getThumbOffsetFromScroll(e,s,n.dir);i.current.style.transform=`translate3d(${r}px, 0, 0)`}},onWheelScroll:e=>{n.viewport&&(n.viewport.scrollLeft=e)},onDragScroll:e=>{n.viewport&&(n.viewport.scrollLeft=getScrollPosition(e,n.dir))}})):"vertical"===t?(0,l.createElement)(D,(0,a.Z)({},f,{ref:r,onThumbPositionChange:()=>{if(n.viewport&&i.current){let e=n.viewport.scrollTop,r=$57acba87d6e25586$var$getThumbOffsetFromScroll(e,s);i.current.style.transform=`translate3d(0, ${r}px, 0)`}},onWheelScroll:e=>{n.viewport&&(n.viewport.scrollTop=e)},onDragScroll:e=>{n.viewport&&(n.viewport.scrollTop=getScrollPosition(e))}})):null}),z=(0,l.forwardRef)((e,r)=>{let{sizes:t,onSizesChange:o,...n}=e,i=g(E,e.__scopeScrollArea),[c,s]=(0,l.useState)(),u=(0,l.useRef)(null),f=(0,d.e)(r,u,i.onScrollbarXChange);return(0,l.useEffect)(()=>{u.current&&s(getComputedStyle(u.current))},[u]),(0,l.createElement)(A,(0,a.Z)({"data-orientation":"horizontal"},n,{ref:f,sizes:t,style:{bottom:0,left:"rtl"===i.dir?"var(--radix-scroll-area-corner-width)":0,right:"ltr"===i.dir?"var(--radix-scroll-area-corner-width)":0,"--radix-scroll-area-thumb-width":$57acba87d6e25586$var$getThumbSize(t)+"px",...e.style},onThumbPointerDown:r=>e.onThumbPointerDown(r.x),onDragScroll:r=>e.onDragScroll(r.x),onWheelScroll:(r,t)=>{if(i.viewport){let l=i.viewport.scrollLeft+r.deltaX;e.onWheelScroll(l),l>0&&l<t&&r.preventDefault()}},onResize:()=>{u.current&&i.viewport&&c&&o({content:i.viewport.scrollWidth,viewport:i.viewport.offsetWidth,scrollbar:{size:u.current.clientWidth,paddingStart:$57acba87d6e25586$var$toInt(c.paddingLeft),paddingEnd:$57acba87d6e25586$var$toInt(c.paddingRight)}})}}))}),D=(0,l.forwardRef)((e,r)=>{let{sizes:t,onSizesChange:o,...n}=e,i=g(E,e.__scopeScrollArea),[c,s]=(0,l.useState)(),u=(0,l.useRef)(null),f=(0,d.e)(r,u,i.onScrollbarYChange);return(0,l.useEffect)(()=>{u.current&&s(getComputedStyle(u.current))},[u]),(0,l.createElement)(A,(0,a.Z)({"data-orientation":"vertical"},n,{ref:f,sizes:t,style:{top:0,right:"ltr"===i.dir?0:void 0,left:"rtl"===i.dir?0:void 0,bottom:"var(--radix-scroll-area-corner-height)","--radix-scroll-area-thumb-height":$57acba87d6e25586$var$getThumbSize(t)+"px",...e.style},onThumbPointerDown:r=>e.onThumbPointerDown(r.y),onDragScroll:r=>e.onDragScroll(r.y),onWheelScroll:(r,t)=>{if(i.viewport){let l=i.viewport.scrollTop+r.deltaY;e.onWheelScroll(l),l>0&&l<t&&r.preventDefault()}},onResize:()=>{u.current&&i.viewport&&c&&o({content:i.viewport.scrollHeight,viewport:i.viewport.offsetHeight,scrollbar:{size:u.current.clientHeight,paddingStart:$57acba87d6e25586$var$toInt(c.paddingTop),paddingEnd:$57acba87d6e25586$var$toInt(c.paddingBottom)}})}}))}),[L,_]=b(E),A=(0,l.forwardRef)((e,r)=>{let{__scopeScrollArea:t,sizes:o,hasThumb:n,onThumbChange:c,onThumbPointerUp:s,onThumbPointerDown:f,onThumbPositionChange:h,onDragScroll:p,onWheelScroll:b,onResize:m,...w}=e,$=g(E,t),[S,y]=(0,l.useState)(null),T=(0,d.e)(r,e=>y(e)),C=(0,l.useRef)(null),R=(0,l.useRef)(""),P=$.viewport,z=o.content-o.viewport,D=(0,u.W)(b),_=(0,u.W)(h),A=$57acba87d6e25586$var$useDebounceCallback(m,10);function handleDragScroll(e){if(C.current){let r=e.clientX-C.current.left,t=e.clientY-C.current.top;p({x:r,y:t})}}return(0,l.useEffect)(()=>{let handleWheel=e=>{let r=e.target,t=null==S?void 0:S.contains(r);t&&D(e,z)};return document.addEventListener("wheel",handleWheel,{passive:!1}),()=>document.removeEventListener("wheel",handleWheel,{passive:!1})},[P,S,z,D]),(0,l.useEffect)(_,[o,_]),$57acba87d6e25586$var$useResizeObserver(S,A),$57acba87d6e25586$var$useResizeObserver($.content,A),(0,l.createElement)(L,{scope:t,scrollbar:S,hasThumb:n,onThumbChange:(0,u.W)(c),onThumbPointerUp:(0,u.W)(s),onThumbPositionChange:_,onThumbPointerDown:(0,u.W)(f)},(0,l.createElement)(i.WV.div,(0,a.Z)({},w,{ref:T,style:{position:"absolute",...w.style},onPointerDown:(0,v.M)(e.onPointerDown,e=>{if(0===e.button){let r=e.target;r.setPointerCapture(e.pointerId),C.current=S.getBoundingClientRect(),R.current=document.body.style.webkitUserSelect,document.body.style.webkitUserSelect="none",$.viewport&&($.viewport.style.scrollBehavior="auto"),handleDragScroll(e)}}),onPointerMove:(0,v.M)(e.onPointerMove,handleDragScroll),onPointerUp:(0,v.M)(e.onPointerUp,e=>{let r=e.target;r.hasPointerCapture(e.pointerId)&&r.releasePointerCapture(e.pointerId),document.body.style.webkitUserSelect=R.current,$.viewport&&($.viewport.style.scrollBehavior=""),C.current=null})})))}),x="ScrollAreaThumb",W=(0,l.forwardRef)((e,r)=>{let{forceMount:t,...o}=e,n=_(x,e.__scopeScrollArea);return(0,l.createElement)(c.z,{present:t||n.hasThumb},(0,l.createElement)(k,(0,a.Z)({ref:r},o)))}),k=(0,l.forwardRef)((e,r)=>{let{__scopeScrollArea:t,style:o,...n}=e,c=g(x,t),s=_(x,t),{onThumbPositionChange:u}=s,f=(0,d.e)(r,e=>s.onThumbChange(e)),h=(0,l.useRef)(),p=$57acba87d6e25586$var$useDebounceCallback(()=>{h.current&&(h.current(),h.current=void 0)},100);return(0,l.useEffect)(()=>{let e=c.viewport;if(e){let handleScroll=()=>{if(p(),!h.current){let r=$57acba87d6e25586$var$addUnlinkedScrollListener(e,u);h.current=r,u()}};return u(),e.addEventListener("scroll",handleScroll),()=>e.removeEventListener("scroll",handleScroll)}},[c.viewport,p,u]),(0,l.createElement)(i.WV.div,(0,a.Z)({"data-state":s.hasThumb?"visible":"hidden"},n,{ref:f,style:{width:"var(--radix-scroll-area-thumb-width)",height:"var(--radix-scroll-area-thumb-height)",...o},onPointerDownCapture:(0,v.M)(e.onPointerDownCapture,e=>{let r=e.target,t=r.getBoundingClientRect(),l=e.clientX-t.left,o=e.clientY-t.top;s.onThumbPointerDown({x:l,y:o})}),onPointerUp:(0,v.M)(e.onPointerUp,s.onThumbPointerUp)}))}),N="ScrollAreaCorner",M=(0,l.forwardRef)((e,r)=>{let t=g(N,e.__scopeScrollArea),o=!!(t.scrollbarX&&t.scrollbarY),n="scroll"!==t.type&&o;return n?(0,l.createElement)(Z,(0,a.Z)({},e,{ref:r})):null}),Z=(0,l.forwardRef)((e,r)=>{let{__scopeScrollArea:t,...o}=e,n=g(N,t),[c,s]=(0,l.useState)(0),[d,u]=(0,l.useState)(0);return $57acba87d6e25586$var$useResizeObserver(n.scrollbarX,()=>{var e;let r=(null===(e=n.scrollbarX)||void 0===e?void 0:e.offsetHeight)||0;n.onCornerHeightChange(r),u(r)}),$57acba87d6e25586$var$useResizeObserver(n.scrollbarY,()=>{var e;let r=(null===(e=n.scrollbarY)||void 0===e?void 0:e.offsetWidth)||0;n.onCornerWidthChange(r),s(r)}),c&&d?(0,l.createElement)(i.WV.div,(0,a.Z)({},o,{ref:r,style:{width:c,height:d,position:"absolute",right:"ltr"===n.dir?0:void 0,left:"rtl"===n.dir?0:void 0,bottom:0,...e.style}})):null});function $57acba87d6e25586$var$toInt(e){return e?parseInt(e,10):0}function $57acba87d6e25586$var$getThumbRatio(e,r){let t=e/r;return isNaN(t)?0:t}function $57acba87d6e25586$var$getThumbSize(e){let r=$57acba87d6e25586$var$getThumbRatio(e.viewport,e.content),t=e.scrollbar.paddingStart+e.scrollbar.paddingEnd,l=(e.scrollbar.size-t)*r;return Math.max(l,18)}function $57acba87d6e25586$var$getScrollPositionFromPointer(e,r,t,l="ltr"){let o=$57acba87d6e25586$var$getThumbSize(t),n=r||o/2,a=t.scrollbar.paddingStart+n,i=t.scrollbar.size-t.scrollbar.paddingEnd-(o-n),c=t.content-t.viewport,s=$57acba87d6e25586$var$linearScale([a,i],"ltr"===l?[0,c]:[-1*c,0]);return s(e)}function $57acba87d6e25586$var$getThumbOffsetFromScroll(e,r,t="ltr"){let l=$57acba87d6e25586$var$getThumbSize(r),o=r.scrollbar.paddingStart+r.scrollbar.paddingEnd,n=r.scrollbar.size-o,a=r.content-r.viewport,i="ltr"===t?[0,a]:[-1*a,0],c=$ae6933e535247d3d$export$7d15b64cf5a3a4c4(e,i),s=$57acba87d6e25586$var$linearScale([0,a],[0,n-l]);return s(c)}function $57acba87d6e25586$var$linearScale(e,r){return t=>{if(e[0]===e[1]||r[0]===r[1])return r[0];let l=(r[1]-r[0])/(e[1]-e[0]);return r[0]+l*(t-e[0])}}let $57acba87d6e25586$var$addUnlinkedScrollListener=(e,r=()=>{})=>{let t={left:e.scrollLeft,top:e.scrollTop},l=0;return!function loop(){let o={left:e.scrollLeft,top:e.scrollTop},n=t.left!==o.left,a=t.top!==o.top;(n||a)&&r(),t=o,l=window.requestAnimationFrame(loop)}(),()=>window.cancelAnimationFrame(l)};function $57acba87d6e25586$var$useDebounceCallback(e,r){let t=(0,u.W)(e),o=(0,l.useRef)(0);return(0,l.useEffect)(()=>()=>window.clearTimeout(o.current),[]),(0,l.useCallback)(()=>{window.clearTimeout(o.current),o.current=window.setTimeout(t,r)},[t,r])}function $57acba87d6e25586$var$useResizeObserver(e,r){let t=(0,u.W)(r);(0,h.b)(()=>{let r=0;if(e){let l=new ResizeObserver(()=>{cancelAnimationFrame(r),r=window.requestAnimationFrame(t)});return l.observe(e),()=>{window.cancelAnimationFrame(r),l.unobserve(e)}}},[e,t])}var O=t(8219);let H={size:{type:"enum",values:["1","2","3"],default:"1",responsive:!0},radius:O.C,scrollbars:{type:"enum",values:["vertical","horizontal","both"],default:"both"}};var I=t(3843),Y=t(6776);let F=l.forwardRef((e,r)=>{let{rest:t,...o}=(0,I.FY)(e),{className:a,style:i,type:c,scrollHideDelay:s="scroll"!==c?0:void 0,dir:d,size:u=H.size.default,radius:f=H.radius.default,scrollbars:h=H.scrollbars.default,...v}=t;return l.createElement($,{type:c,scrollHideDelay:s,className:n()("rt-ScrollAreaRoot",a,(0,I.we)(o)),style:i},l.createElement(S,{...v,ref:r,className:"rt-ScrollAreaViewport"}),l.createElement("div",{className:"rt-ScrollAreaViewportFocusRing"}),"vertical"!==h?l.createElement(y,{"data-radius":f,orientation:"horizontal",className:n()("rt-ScrollAreaScrollbar",(0,Y.g)(u,"rt-r-size"))},l.createElement(W,{className:"rt-ScrollAreaThumb"})):null,"horizontal"!==h?l.createElement(y,{"data-radius":f,orientation:"vertical",className:n()("rt-ScrollAreaScrollbar",(0,Y.g)(u,"rt-r-size"))},l.createElement(W,{className:"rt-ScrollAreaThumb"})):null,"both"===h?l.createElement(M,{className:"rt-ScrollAreaCorner"}):null)});F.displayName="ScrollArea"},8219:function(e,r,t){"use strict";t.d(r,{C:function(){return o}});var l=t(269);let o={type:"enum",values:l.yT.radius.values,default:void 0}},2795:function(e,r,t){"use strict";t.d(r,{Z:function(){return o}});var l=t(5711);/**
 * @license lucide-react v0.359.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */let o=(0,l.Z)("Code",[["polyline",{points:"16 18 22 12 16 6",key:"z7tu5w"}],["polyline",{points:"8 6 2 12 8 18",key:"1eg1df"}]])},3025:function(e,r,t){"use strict";t.d(r,{Z:function(){return o}});var l=t(5711);/**
 * @license lucide-react v0.359.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */let o=(0,l.Z)("Download",[["path",{d:"M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4",key:"ih7n3h"}],["polyline",{points:"7 10 12 15 17 10",key:"2ggqvy"}],["line",{x1:"12",x2:"12",y1:"15",y2:"3",key:"1vk2je"}]])},9162:function(e,r,t){"use strict";t.d(r,{Z:function(){return o}});var l=t(5711);/**
 * @license lucide-react v0.359.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */let o=(0,l.Z)("Github",[["path",{d:"M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4",key:"tonef"}],["path",{d:"M9 18c-4.51 2-5-2-7-2",key:"9comsn"}]])},3184:function(e,r,t){"use strict";t.d(r,{Z:function(){return o}});var l=t(5711);/**
 * @license lucide-react v0.359.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */let o=(0,l.Z)("PanelsTopLeft",[["rect",{width:"18",height:"18",x:"3",y:"3",rx:"2",key:"afitv7"}],["path",{d:"M3 9h18",key:"1pudct"}],["path",{d:"M9 21V9",key:"1oto5p"}]])},4298:function(e,r,t){e.exports=t(5354)}}]);