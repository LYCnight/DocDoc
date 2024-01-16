/**
 * @license Copyright (c) 2003-2022, CKSource Holding sp. z o.o. All rights reserved.
 * For licensing, see LICENSE.md.
 */

import { ClassicEditor } from '@ckeditor/ckeditor5-editor-classic';
import { Essentials } from '@ckeditor/ckeditor5-essentials';
import { Paragraph } from '@ckeditor/ckeditor5-paragraph';
import { Heading } from '@ckeditor/ckeditor5-heading';
import { List } from '@ckeditor/ckeditor5-list';
import { Bold, Italic } from '@ckeditor/ckeditor5-basic-styles';

import Plugin from '@ckeditor/ckeditor5-core/src/plugin';
import ButtonView from '@ckeditor/ckeditor5-ui/src/button/buttonview';
import CKEditorInspector from '@ckeditor/ckeditor5-inspector';

import getRangeText from './utils.js';

class Timestamp extends Plugin {
    init() {
        console.log( 'Timestamp was initialized.' );
        const editor = this.editor;
        // The button must be registered among the UI components of the editor
        // to be displayed in the toolbar.
        editor.ui.componentFactory.add( 'timestamp', () => {
            // We also need to register our button in the editor’s UI componentFactory, so it can be displayed in the toolbar. 
            // The button will be an instance of ButtonView.
            const button = new ButtonView();

            button.set( {
                label: 'Timestamp',
                withText: true
            } );

            /*************** plugin 真正的功能逻辑代码 ************/
            // Execute a callback function when the button is clicked.
            button.on( 'execute', () => {
                const now = new Date();

                // Change the model using the model writer. 
                editor.model.change( writer => {   // change 和 write 能够改变编辑框中的内容文本
                    // Insert the text at the user's current position.
                    editor.model.insertContent( writer.createText( now.toString() ) );
                } );
            } );            
            
            /*****************************************************/    
            return button;
        } );
    }
}


class ShowSelection extends Plugin {
    init() {
        console.log( 'ShowSelection was initialized.' );
        const editor = this.editor;
        // The button must be registered among the UI components of the editor
        // to be displayed in the toolbar.
        editor.ui.componentFactory.add( 'showSectool', () => {
            // We also need to register our button in the editor’s UI componentFactory, so it can be displayed in the toolbar. 
            // The button will be an instance of ButtonView.
            const button = new ButtonView();

            button.set( {
                label: 'ShowSec',
                withText: true
            } );

            /*************** plugin 真正的功能逻辑代码 ************/
            // Execute a callback function when the button is clicked.
            button.on( 'execute', () => {
                const model = this.editor.model;
                const selection = model.document.selection;
                const range = editor.model.document.selection.getFirstRange();
                console.log("getFirstRange succeeded!")
                const text = getRangeText(range) 
                console.log(text);

                // 直接替换选区内容
                editor.model.change(writer => {
                    editor.model.insertContent(writer.createText('foo'));
                });

                // 在选区前插入
                // editor.model.change( writer => {
                //     writer.insertText( 'foo：', editor.model.document.selection.getFirstPosition() );
                // } );

                // 在选区后插入
                // editor.model.change( writer => {
                //     writer.insertText( 'foo：', editor.model.document.selection.getLastPosition() );
                // } );
            } );            
            
            /*****************************************************/    
            return button;
        } );
    }
}


class AI extends Plugin {
    init() {
        console.log( 'AI was initialized.' );
        const editor = this.editor;
        // The button must be registered among the UI components of the editor
        // to be displayed in the toolbar.
        editor.ui.componentFactory.add( 'AItool', () => {
            // We also need to register our button in the editor’s UI componentFactory, so it can be displayed in the toolbar. 
            // The button will be an instance of ButtonView.
            const button = new ButtonView();

            button.set( {
                label: 'AI',    // 按钮的默认文字
                withText: true
            } );

            /*************** plugin 真正的功能逻辑代码 ************/
            // Execute a callback function when the button is clicked.
            button.on( 'execute', async () => {
                try {
                    const response = await fetch('http://127.0.0.1:8000/hello');
                    if (!response.ok) {
                        throw new Error('Network response was not ok.');
                    }

                    const data = await response.json();
                    editor.model.change(writer => {
                        // editor.model.insertContent(writer.createText("测试"));
                        console.log(typeof(data));  // String
                        console.log(data);  // 你好，我是AI，运行在后端
                        editor.model.insertContent(writer.createText(data));
                    });
                } catch (error) {
                    console.error('There has been a problem with your fetch operation:', error);
                }
            } );            
            
            /*****************************************************/    
            return button;
        } );
    }
}

class AIHi extends Plugin {
    init() {
        console.log( 'AIHi was initialized.' );
        const editor = this.editor;
        // The button must be registered among the UI components of the editor
        // to be displayed in the toolbar.
        editor.ui.componentFactory.add( 'AIHitool', () => {
            // We also need to register our button in the editor’s UI componentFactory, so it can be displayed in the toolbar. 
            // The button will be an instance of ButtonView.
            const button = new ButtonView();

            button.set( {
                label: 'AIHi',    // 按钮的默认文字
                withText: true
            } );

            /*************** plugin 真正的功能逻辑代码 ************/
            // Execute a callback function when the button is clicked.
            button.on( 'execute', async () => {
                try {
                    const response = await fetch('http://127.0.0.1:8000/AIHi');
                    if (!response.ok) {
                        throw new Error('Network response was not ok.');
                    }

                    const data = await response.json();
                    editor.model.change(writer => {
                        // editor.model.insertContent(writer.createText("测试"));
                        console.log(typeof(data));  // String
                        console.log(data);  // 你好，我是AI，运行在后端
                        editor.model.insertContent(writer.createText(data));
                    });
                } catch (error) {
                    console.error('There has been a problem with your fetch operation:', error);
                }
            } );            
            
            /*****************************************************/    
            return button;
        } );
    }
}

class AIGen extends Plugin {
    init() {
        console.log( 'AIGen was initialized.' );
        const editor = this.editor;
        // The button must be registered among the UI components of the editor
        // to be displayed in the toolbar.
        editor.ui.componentFactory.add( 'AIGentool', () => {        // "" 里为工具的变量名，在 toolbar 中被引用
            // We also need to register our button in the editor’s UI componentFactory, so it can be displayed in the toolbar. 
            // The button will be an instance of ButtonView.
            const button = new ButtonView();

            button.set( {
                label: 'AIGen',    // 按钮的默认文字
                withText: true
            } );

            /*************** plugin 真正的功能逻辑代码 ************/
            // Execute a callback function when the button is clicked.
            button.on( 'execute', async () => {
                try {
                    console.log( 'AIGen\'s \'execute\' has been trigered .' );
                    const response = await fetch('http://127.0.0.1:8000/AIGen');
                    if (!response.ok) {
                        throw new Error('Network response was not ok.');
                    }
                    console.log( 'AIGen\'s response has been got.' );

                    const data = await response.json();
                    editor.model.change(writer => {
                        // editor.model.insertContent(writer.createText("测试"));
                        console.log(typeof(data));  // String
                        console.log( 'Trying to write the response to the editor' );
                        editor.model.insertContent(writer.createText(data));
                    });
                } catch (error) {
                    console.error('There has been a problem with your fetch operation:', error);
                }
            } );            
            
            /*****************************************************/    
            return button;
        } );
    }
}

class AIContinue extends Plugin {
    init() {
        console.log( 'AIContinue was initialized.' );
        const editor = this.editor;
        // The button must be registered among the UI components of the editor
        // to be displayed in the toolbar.
        editor.ui.componentFactory.add( 'AIContinuetool', () => {        // '' 里为工具的变量名，在 toolbar 中被引用
            // We also need to register our button in the editor’s UI componentFactory, so it can be displayed in the toolbar. 
            // The button will be an instance of ButtonView.
            const button = new ButtonView();

            button.set( {
                label: 'AI续写',    // 按钮的默认文字
                withText: true
            } );

            /*************** plugin 真正的功能逻辑代码 ************/
            // Execute a callback function when the button is clicked.
            button.on( 'execute', async () => {
                try {
                    const model = this.editor.model;
                    const selection = model.document.selection;
                    const range = editor.model.document.selection.getFirstRange();
                    const text = getRangeText(range)    // 被选中的文本
                    console.log(text);

                    // 定义要发送的数据
                    const postData = {
                        text: text
                    };

                    // 发送 post 请求
                    const response = await fetch('http://127.0.0.1:8000/AIContinue',{
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json' // 指定请求体的类型为JSON
                        },
                        body: JSON.stringify(postData) // 将数据转换为JSON格式并设置为请求体
                    });  
                    
                    if (!response.ok) {
                        throw new Error('Network response was not ok.');
                    }
                    console.log( 'AIContinue\'s response has been got.' );

                    const data = await response.json();
                    console.log(data)

                    editor.model.change( writer => {
                        //getLastPosition() 在选中文本的末尾插入续写内容
                        writer.insertText( data, editor.model.document.selection.getLastPosition() );
                    } );

                } catch (error) {
                    console.error('There has been a problem with your fetch operation:', error);
                }
            } );            
            
            /*****************************************************/    
            return button;
        } );
    }
}


class AIImprove extends Plugin {
    init() {
        console.log( 'AIImprove was initialized.' );
        const editor = this.editor;
        // The button must be registered among the UI components of the editor
        // to be displayed in the toolbar.
        editor.ui.componentFactory.add( 'AIImprovetool', () => {        // '' 里为工具的变量名，在 toolbar 中被引用
            // We also need to register our button in the editor’s UI componentFactory, so it can be displayed in the toolbar. 
            // The button will be an instance of ButtonView.
            const button = new ButtonView();

            button.set( {
                label: 'AI优化',    // 按钮的默认文字
                withText: true
            } );

            /*************** plugin 真正的功能逻辑代码 ************/
            // Execute a callback function when the button is clicked.
            button.on( 'execute', async () => {
                try {
                    const model = this.editor.model;
                    const selection = model.document.selection;
                    const range = editor.model.document.selection.getFirstRange();
                    const text = getRangeText(range)    // 被选中的文本
                    console.log(text);

                    // 定义要发送的数据
                    const postData = {
                        text: text
                    };

                    // 发送 post 请求
                    const response = await fetch('http://127.0.0.1:8000/AIImprove',{
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json' // 指定请求体的类型为JSON
                        },
                        body: JSON.stringify(postData) // 将数据转换为JSON格式并设置为请求体
                    });  
                    
                    if (!response.ok) {
                        throw new Error('Network response was not ok.');
                    }
                    console.log( 'AIContinue\'s response has been got.' );

                    const data = await response.json();
                    console.log(data)

                    editor.model.change(writer => {
                        // 直接把选中的内容替换掉
                        editor.model.insertContent(writer.createText(data));
                    });

                } catch (error) {
                    console.error('There has been a problem with your fetch operation:', error);
                }
            } );            
            
            /*****************************************************/    
            return button;
        } );
    }
}





const editor = await ClassicEditor
	.create( document.querySelector( '#editor' ), {
		plugins: [ Essentials, Paragraph, Heading, List, Bold, Italic, Timestamp, AI, AIHi, AIGen, AIContinue, AIImprove, ShowSelection],
		toolbar: [ 'heading', 'bold', 'italic', 'numberedList', 'bulletedList', 'timestamp', 'AItool', 'AIHitool', 'AIGentool', 'AIContinuetool', 'AIImprovetool', 'showSectool' ]
	} )
	.then( editor => {
		console.log( 'Editor was initialized', editor );
        CKEditorInspector.attach( editor );
	} )
	.catch( error => {
		console.error( error.stack );
	} );


// Add the global `editor` variable (only needed for debugging).
window.editor = editor;


