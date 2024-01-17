/**
 * @license Copyright (c) 2014-2024, CKSource Holding sp. z o.o. All rights reserved.
 * For licensing, see LICENSE.md or https://ckeditor.com/legal/ckeditor-oss-license
 */

import { ClassicEditor } from '@ckeditor/ckeditor5-editor-classic';

import { Alignment } from '@ckeditor/ckeditor5-alignment';
import { Autoformat } from '@ckeditor/ckeditor5-autoformat';
import { Bold, Italic } from '@ckeditor/ckeditor5-basic-styles';
import { BlockQuote } from '@ckeditor/ckeditor5-block-quote';
import type { EditorConfig } from '@ckeditor/ckeditor5-core';
import { Essentials } from '@ckeditor/ckeditor5-essentials';
import { Heading } from '@ckeditor/ckeditor5-heading';
import {
	Image,
	ImageCaption,
	ImageStyle,
	ImageToolbar,
	ImageUpload
} from '@ckeditor/ckeditor5-image';
import { Indent } from '@ckeditor/ckeditor5-indent';
import { Link } from '@ckeditor/ckeditor5-link';
import { List } from '@ckeditor/ckeditor5-list';
import { MediaEmbed } from '@ckeditor/ckeditor5-media-embed';
import { Paragraph } from '@ckeditor/ckeditor5-paragraph';
import { PasteFromOffice } from '@ckeditor/ckeditor5-paste-from-office';
import { Table, TableToolbar } from '@ckeditor/ckeditor5-table';
import { TextTransformation } from '@ckeditor/ckeditor5-typing';
import { Undo } from '@ckeditor/ckeditor5-undo';

// You can read more about extending the build with additional plugins in the "Installing plugins" guide.
// See https://ckeditor.com/docs/ckeditor5/latest/installation/plugins/installing-plugins.html for details.

import Plugin from '@ckeditor/ckeditor5-core/src/plugin';
import ButtonView from '@ckeditor/ckeditor5-ui/src/button/buttonview';
import getRangeText from './utils';

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
							// writer.insertText( data, editor.model.document.selection.getLastPosition() ); //暂时出现报错

							// 直接把选中的内容替换掉
							editor.model.insertContent(writer.createText(data));
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




class Editor extends ClassicEditor {
	public static override builtinPlugins = [
		Alignment,
		Autoformat,
		BlockQuote,
		Bold,
		Essentials,
		Heading,
		Image,
		ImageCaption,
		ImageStyle,
		ImageToolbar,
		ImageUpload,
		Indent,
		Italic,
		Link,
		List,
		MediaEmbed,
		Paragraph,
		PasteFromOffice,
		Table,
		TableToolbar,
		TextTransformation,
		Undo,
		AI, AIHi, AIGen, AIContinue, AIImprove
	];

	public static override defaultConfig: EditorConfig = {
		toolbar: {
			items: [
				'alignment',
				'|',
				'heading',
				'bold',
				'italic',
				'link',
				'bulletedList',
				'numberedList',
				'|',
				'outdent',
				'indent',
				'|',
				'imageUpload',
				'blockQuote',
				'insertTable',
				'mediaEmbed',
				'undo',
				'redo',
				'|', 'AItool', 'AIHitool', 'AIGentool', 'AIContinuetool', 'AIImprovetool'
			]
		},
		language: 'zh-cn',
		image: {
			toolbar: [
				'imageTextAlternative',
				'toggleImageCaption',
				'imageStyle:inline',
				'imageStyle:block',
				'imageStyle:side'
			]
		},
		table: {
			contentToolbar: [
				'tableColumn',
				'tableRow',
				'mergeTableCells'
			]
		}
	};
}

export default Editor;
