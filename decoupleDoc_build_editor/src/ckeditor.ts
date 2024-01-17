import { DecoupledEditor } from '@ckeditor/ckeditor5-editor-decoupled';

import { UploadAdapter } from '@ckeditor/ckeditor5-adapter-ckfinder';
import { Alignment } from '@ckeditor/ckeditor5-alignment';
import { Autoformat } from '@ckeditor/ckeditor5-autoformat';
import { Autosave } from '@ckeditor/ckeditor5-autosave';
import {
	Bold,
	Code,
	Italic,
	Strikethrough,
	Subscript,
	Superscript,
	Underline
} from '@ckeditor/ckeditor5-basic-styles';
import { BlockQuote } from '@ckeditor/ckeditor5-block-quote';
import { CloudServices } from '@ckeditor/ckeditor5-cloud-services';
import { CodeBlock } from '@ckeditor/ckeditor5-code-block';
import type { EditorConfig } from '@ckeditor/ckeditor5-core';
import { Essentials } from '@ckeditor/ckeditor5-essentials';
import { FindAndReplace } from '@ckeditor/ckeditor5-find-and-replace';
import { FontBackgroundColor, FontColor, FontFamily, FontSize } from '@ckeditor/ckeditor5-font';
import { Heading, Title } from '@ckeditor/ckeditor5-heading';
import { Highlight } from '@ckeditor/ckeditor5-highlight';
import { HorizontalLine } from '@ckeditor/ckeditor5-horizontal-line';
import { HtmlEmbed } from '@ckeditor/ckeditor5-html-embed';
import {
	DataFilter,
	DataSchema,
	GeneralHtmlSupport,
	HtmlComment
} from '@ckeditor/ckeditor5-html-support';
import {
	AutoImage,
	Image,
	ImageCaption,
	ImageInsert,
	ImageResize,
	ImageStyle,
	ImageToolbar,
	ImageUpload
} from '@ckeditor/ckeditor5-image';
import { Indent, IndentBlock } from '@ckeditor/ckeditor5-indent';
import { TextPartLanguage } from '@ckeditor/ckeditor5-language';
import { AutoLink, Link, LinkImage } from '@ckeditor/ckeditor5-link';
import { List, ListProperties, TodoList } from '@ckeditor/ckeditor5-list';
import { Markdown } from '@ckeditor/ckeditor5-markdown-gfm';
import { MediaEmbed, MediaEmbedToolbar } from '@ckeditor/ckeditor5-media-embed';
import { Mention } from '@ckeditor/ckeditor5-mention';
import { PageBreak } from '@ckeditor/ckeditor5-page-break';
import { Paragraph } from '@ckeditor/ckeditor5-paragraph';
import { PasteFromOffice } from '@ckeditor/ckeditor5-paste-from-office';
import { RemoveFormat } from '@ckeditor/ckeditor5-remove-format';
import { StandardEditingMode } from '@ckeditor/ckeditor5-restricted-editing';
import { SelectAll } from '@ckeditor/ckeditor5-select-all';
import { ShowBlocks } from '@ckeditor/ckeditor5-show-blocks';
import { SourceEditing } from '@ckeditor/ckeditor5-source-editing';
import {
	SpecialCharacters,
	SpecialCharactersArrows,
	SpecialCharactersCurrency,
	SpecialCharactersEssentials,
	SpecialCharactersLatin,
	SpecialCharactersMathematical,
	SpecialCharactersText
} from '@ckeditor/ckeditor5-special-characters';
import { Style } from '@ckeditor/ckeditor5-style';
import {
	Table,
	TableCaption,
	TableCellProperties,
	TableColumnResize,
	TableProperties,
	TableToolbar
} from '@ckeditor/ckeditor5-table';
import { TextTransformation } from '@ckeditor/ckeditor5-typing';
import { Undo } from '@ckeditor/ckeditor5-undo';
import { EditorWatchdog } from '@ckeditor/ckeditor5-watchdog';
import { WordCount } from '@ckeditor/ckeditor5-word-count';

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


class Editor extends DecoupledEditor {
	public static override builtinPlugins = [
		Alignment,
		AutoImage,
		AutoLink,
		Autoformat,
		Autosave,
		BlockQuote,
		Bold,
		CloudServices,
		Code,
		CodeBlock,
		DataFilter,
		DataSchema,
		Essentials,
		FindAndReplace,
		FontBackgroundColor,
		FontColor,
		FontFamily,
		FontSize,
		GeneralHtmlSupport,
		Heading,
		Highlight,
		HorizontalLine,
		HtmlComment,
		HtmlEmbed,
		Image,
		ImageCaption,
		ImageInsert,
		ImageResize,
		ImageStyle,
		ImageToolbar,
		ImageUpload,
		Indent,
		IndentBlock,
		Italic,
		Link,
		LinkImage,
		List,
		ListProperties,
		Markdown,
		MediaEmbed,
		MediaEmbedToolbar,
		Mention,
		PageBreak,
		Paragraph,
		PasteFromOffice,
		RemoveFormat,
		SelectAll,
		ShowBlocks,
		SourceEditing,
		SpecialCharacters,
		SpecialCharactersArrows,
		SpecialCharactersCurrency,
		SpecialCharactersEssentials,
		SpecialCharactersLatin,
		SpecialCharactersMathematical,
		SpecialCharactersText,
		StandardEditingMode,
		Strikethrough,
		Style,
		Subscript,
		Superscript,
		Table,
		TableCaption,
		TableCellProperties,
		TableColumnResize,
		TableProperties,
		TableToolbar,
		TextPartLanguage,
		TextTransformation,
		Title,
		TodoList,
		Underline,
		Undo,
		UploadAdapter,
		WordCount,
		AI, AIHi, AIGen, AIContinue, AIImprove
	];

	public static override defaultConfig: EditorConfig = {
		toolbar: {
			items: [
				'heading',
				'|',
				'fontSize',
				'fontFamily',
				'fontColor',
				'fontBackgroundColor',
				'|',
				'bold',
				'italic',
				'numberedList',
				'bulletedList',
				'todoList',
				'underline',
				'strikethrough',
				'subscript',
				'superscript',
				'|',
				'alignment',
				'outdent',
				'indent',
				'|',
				'AItool', 'AIHitool', 'AIGentool', 'AIContinuetool', 'AIImprovetool',
				'|',
				'link',
				'blockQuote',
				'imageUpload',
				'insertTable',
				'mediaEmbed',
				'|',
				'undo',
				'redo',
				'code',
				'codeBlock',
				'findAndReplace',
				'highlight',
				'horizontalLine',
				'htmlEmbed',
				'imageInsert',
				'pageBreak',
				'removeFormat',
				'selectAll',
				'showBlocks',
				'sourceEditing',
				'specialCharacters',
				'restrictedEditingException',
				'|',
				'style',
				'|',
				'textPartLanguage',
				'|'
			]
		},
		language: 'zh-cn',
		image: {
			toolbar: [
				'imageTextAlternative',
				'toggleImageCaption',
				'imageStyle:inline',
				'imageStyle:block',
				'imageStyle:side',
				'linkImage'
			]
		},
		table: {
			contentToolbar: [
				'tableColumn',
				'tableRow',
				'mergeTableCells',
				'tableCellProperties',
				'tableProperties'
			]
		}
	};
}

export default { Editor, EditorWatchdog };
