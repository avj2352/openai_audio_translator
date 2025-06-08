import { useContext, type FC, type JSX, useEffect, useState } from 'react';
import { useEditor } from '@tiptap/react';
import StarterKit from '@tiptap/starter-kit';
import { RichTextEditor } from '@mantine/tiptap';
import { AppContext } from '@/services/AppContext';
import '@mantine/tiptap/styles.css';



const TextEditor: FC = ():JSX.Element => {
  // context
  const appContext = useContext(AppContext);
  const [editorContent, setEditorContent] = useState<string>(appContext.transcribedText);

  // init editor
  const editor = useEditor({
    extensions: [StarterKit],
    content: editorContent,
    onUpdate({ editor }) {
      setEditorContent(editor.getHTML());
    },
  });
  
  // when context api content changes, update editor
  useEffect(()=>{
    console.log('Text Editor - updated content:', appContext.transcribedText);
    if (editor && appContext.transcribedText !== editor.getHTML()) {
      // set editor content when state change externally
      editor.commands.setContent(appContext.transcribedText);
    }
  },[appContext.transcribedText]);

  return (
    <RichTextEditor editor={editor}>
      <RichTextEditor.Toolbar sticky stickyOffset="var(--docs-header-height)">
        <RichTextEditor.ControlsGroup>
          <RichTextEditor.Bold />
          <RichTextEditor.Italic />
          <RichTextEditor.Strikethrough />
          <RichTextEditor.ClearFormatting />
        </RichTextEditor.ControlsGroup>
      </RichTextEditor.Toolbar>

      <RichTextEditor.Content />
    </RichTextEditor>
  );
};


export default TextEditor;
