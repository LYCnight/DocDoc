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
                    const response = await fetch('http://127.0.0.1:8001/hello');
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
                    const response = await fetch('http://127.0.0.1:8001/AIHi');
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


ClassicEditor
	.create( document.querySelector( '#editor' ), {
		plugins: [ Essentials, Paragraph, Heading, List, Bold, Italic, Timestamp, AI, AIHi ],
		toolbar: [ 'heading', 'bold', 'italic', 'numberedList', 'bulletedList', 'timestamp', 'AItool', 'AIHitool']
	} )
	.then( editor => {
		console.log( 'Editor was initialized', editor );
	} )
	.catch( error => {
		console.error( error.stack );
	} );


