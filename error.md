ERROR
Module build failed (from ./node_modules/babel-loader/lib/index.js):
SyntaxError: /home/mailfox/survival-game/web-frontend/src/App.js: Identifier 'App' has already been declared. (29:9)

  27 | import axios from 'axios';
  28 |
> 29 | function App() {
     |          ^
  30 |   useEffect(() => {
  31 |     axios.get('http://localhost:8000/')
  32 |       .then(response => console.log('Ответ от бэкенда:', response.data))
    at constructor (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:357:19)
    at FlowParserMixin.raise (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:6600:19)
    at FlowScopeHandler.checkRedeclarationInScope (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:1617:19)
    at FlowScopeHandler.declareName (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:1583:12)
    at FlowScopeHandler.declareName (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:1684:11)
    at FlowParserMixin.registerFunctionStatementId (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:13335:16)
    at FlowParserMixin.parseFunction (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:13319:12)
    at FlowParserMixin.parseFunctionStatement (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:12998:17)
    at FlowParserMixin.parseStatementContent (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:12665:21)
    at FlowParserMixin.parseStatementLike (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:12641:17)
    at FlowParserMixin.parseStatementLike (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:2919:24)
    at FlowParserMixin.parseModuleItem (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:12618:17)
    at FlowParserMixin.parseBlockOrModuleBlockBody (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:13189:36)
    at FlowParserMixin.parseBlockBody (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:13182:10)
    at FlowParserMixin.parseProgram (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:12511:10)
    at FlowParserMixin.parseTopLevel (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:12501:25)
    at FlowParserMixin.parseTopLevel (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:3688:28)
    at FlowParserMixin.parse (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:14362:10)
    at parse (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:14396:38)
    at parser (/home/mailfox/survival-game/web-frontend/node_modules/@babel/core/lib/parser/index.js:41:34)
    at parser.next (<anonymous>)
    at normalizeFile (/home/mailfox/survival-game/web-frontend/node_modules/@babel/core/lib/transformation/normalize-file.js:64:37)
    at normalizeFile.next (<anonymous>)
    at run (/home/mailfox/survival-game/web-frontend/node_modules/@babel/core/lib/transformation/index.js:22:50)
    at run.next (<anonymous>)
    at transform (/home/mailfox/survival-game/web-frontend/node_modules/@babel/core/lib/transform.js:22:33)
    at transform.next (<anonymous>)
    at step (/home/mailfox/survival-game/web-frontend/node_modules/gensync/index.js:261:32)
    at /home/mailfox/survival-game/web-frontend/node_modules/gensync/index.js:273:13
    at async.call.result.err.err (/home/mailfox/survival-game/web-frontend/node_modules/gensync/index.js:223:11)
./src/App.js@http://localhost:3000/static/js/bundle.js:21773:7
options.factory@http://localhost:3000/static/js/bundle.js:22652:30
__webpack_require__@http://localhost:3000/static/js/bundle.js:22049:32
fn@http://localhost:3000/static/js/bundle.js:22280:21
hotRequire@http://localhost:3000/static/js/bundle.js:22635:61
./src/index.js@http://localhost:3000/static/js/bundle.js:21896:81
options.factory@http://localhost:3000/static/js/bundle.js:22652:30
__webpack_require__@http://localhost:3000/static/js/bundle.js:22049:32
@http://localhost:3000/static/js/bundle.js:23245:56
@http://localhost:3000/static/js/bundle.js:23247:12
ERROR in ./src/App.js
Module build failed (from ./node_modules/babel-loader/lib/index.js):
SyntaxError: /home/mailfox/survival-game/web-frontend/src/App.js: Identifier 'App' has already been declared. (15:9)

  13 | import Inventory from './components/Inventory';
  14 |
> 15 | function App() {
     |          ^
  16 |   return (
  17 |     <div className="App">
  18 |       <Player id={1} />
    at constructor (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:357:19)
    at FlowParserMixin.raise (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:6600:19)
    at FlowScopeHandler.checkRedeclarationInScope (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:1617:19)
    at FlowScopeHandler.declareName (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:1583:12)
    at FlowScopeHandler.declareName (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:1684:11)
    at FlowParserMixin.registerFunctionStatementId (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:13335:16)
    at FlowParserMixin.parseFunction (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:13319:12)
    at FlowParserMixin.parseFunctionStatement (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:12998:17)
    at FlowParserMixin.parseStatementContent (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:12665:21)
    at FlowParserMixin.parseStatementLike (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:12641:17)
    at FlowParserMixin.parseStatementLike (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:2919:24)
    at FlowParserMixin.parseModuleItem (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:12618:17)
    at FlowParserMixin.parseBlockOrModuleBlockBody (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:13189:36)
    at FlowParserMixin.parseBlockBody (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:13182:10)
    at FlowParserMixin.parseProgram (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:12511:10)
    at FlowParserMixin.parseTopLevel (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:12501:25)
    at FlowParserMixin.parseTopLevel (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:3688:28)
    at FlowParserMixin.parse (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:14362:10)
    at parse (/home/mailfox/survival-game/web-frontend/node_modules/@babel/parser/lib/index.js:14396:38)
    at parser (/home/mailfox/survival-game/web-frontend/node_modules/@babel/core/lib/parser/index.js:41:34)
    at parser.next (<anonymous>)
    at normalizeFile (/home/mailfox/survival-game/web-frontend/node_modules/@babel/core/lib/transformation/normalize-file.js:64:37)
    at normalizeFile.next (<anonymous>)
    at run (/home/mailfox/survival-game/web-frontend/node_modules/@babel/core/lib/transformation/index.js:22:50)
    at run.next (<anonymous>)
    at transform (/home/mailfox/survival-game/web-frontend/node_modules/@babel/core/lib/transform.js:22:33)
    at transform.next (<anonymous>)
    at step (/home/mailfox/survival-game/web-frontend/node_modules/gensync/index.js:261:32)
    at /home/mailfox/survival-game/web-frontend/node_modules/gensync/index.js:273:13
    at async.call.result.err.err (/home/mailfox/survival-game/web-frontend/node_modules/gensync/index.js:223:11)
    at /home/mailfox/survival-game/web-frontend/node_modules/gensync/index.js:189:28
    at /home/mailfox/survival-game/web-frontend/node_modules/@babel/core/lib/gensync-utils/async.js:67:7
    at /home/mailfox/survival-game/web-frontend/node_modules/gensync/index.js:113:33
    at step (/home/mailfox/survival-game/web-frontend/node_modules/gensync/index.js:287:14)
    at /home/mailfox/survival-game/web-frontend/node_modules/gensync/index.js:273:13
    at async.call.result.err.err (/home/mailfox/survival-game/web-frontend/node_modules/gensync/index.js:223:11)
ERROR
[eslint] 
src/App.js
  Line 15:9:  Parsing error: Identifier 'App' has already been declared. (15:9)

