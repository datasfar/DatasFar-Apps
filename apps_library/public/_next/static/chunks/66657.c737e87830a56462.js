(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[66657,57996],{66657:function(e,n,t){"use strict";var s=t(64836);Object.defineProperty(n,"__esModule",{value:!0}),n.default=void 0;var d=s(t(83873)).default;n.default=d},83873:function(e){"use strict";function neon(e){e.languages.neon={comment:{pattern:/#.*/,greedy:!0},datetime:{pattern:/(^|[[{(=:,\s])\d\d\d\d-\d\d?-\d\d?(?:(?:[Tt]| +)\d\d?:\d\d:\d\d(?:\.\d*)? *(?:Z|[-+]\d\d?(?::?\d\d)?)?)?(?=$|[\]}),\s])/,lookbehind:!0,alias:"number"},key:{pattern:/(^|[[{(,\s])[^,:=[\]{}()'"\s]+(?=\s*:(?:$|[\]}),\s])|\s*=)/,lookbehind:!0,alias:"atrule"},number:{pattern:/(^|[[{(=:,\s])[+-]?(?:0x[\da-fA-F]+|0o[0-7]+|0b[01]+|(?:\d+(?:\.\d*)?|\.?\d+)(?:[eE][+-]?\d+)?)(?=$|[\]}),:=\s])/,lookbehind:!0},boolean:{pattern:/(^|[[{(=:,\s])(?:false|no|true|yes)(?=$|[\]}),:=\s])/i,lookbehind:!0},null:{pattern:/(^|[[{(=:,\s])(?:null)(?=$|[\]}),:=\s])/i,lookbehind:!0,alias:"keyword"},string:{pattern:/(^|[[{(=:,\s])(?:('''|""")\r?\n(?:(?:[^\r\n]|\r?\n(?![\t ]*\2))*\r?\n)?[\t ]*\2|'[^'\r\n]*'|"(?:\\.|[^\\"\r\n])*")/,lookbehind:!0,greedy:!0},literal:{pattern:/(^|[[{(=:,\s])(?:[^#"',:=[\]{}()\s`-]|[:-][^"',=[\]{}()\s])(?:[^,:=\]})(\s]|:(?![\s,\]})]|$)|[ \t]+[^#,:=\]})(\s])*/,lookbehind:!0,alias:"string"},punctuation:/[,:=[\]{}()-]/}}e.exports=neon,neon.displayName="neon",neon.aliases=[]},64836:function(e){function _interopRequireDefault(e){return e&&e.__esModule?e:{default:e}}e.exports=_interopRequireDefault,e.exports.__esModule=!0,e.exports.default=e.exports}}]);