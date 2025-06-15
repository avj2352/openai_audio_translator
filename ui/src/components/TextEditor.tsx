import { type FC, type JSX, useEffect, useState } from 'react';
import { useEditor } from '@tiptap/react';
import { Stack, Button } from '@mantine/core';
import StarterKit from '@tiptap/starter-kit';
import { RichTextEditor } from '@mantine/tiptap';
import '@mantine/tiptap/styles.css';

type ITextEditorProps = {
  content: string,
  submitBtnLabel?: string,
  onSubmit: (content: string) => void
};

const TextEditor: FC<ITextEditorProps> = ({ content, submitBtnLabel, onSubmit }):JSX.Element => {
  // context
  const [editorContent, setEditorContent] = useState<string>(content);
  const btnLabel: string =  submitBtnLabel ?? 'Submit';

  // init editor
  const editor = useEditor({
    extensions: [StarterKit],
    content: editorContent,
    onUpdate({ editor }) {
      console.log('editor content: ', editor.getHTML());
      setEditorContent(editor.getHTML());
    },
  });

  // ..evt handlers
  const handleSubmit = () => onSubmit(editorContent);
  
  // when context api content changes, update editor
  useEffect(()=>{
    // console.log('Text Editor - updated content:', content);
    if (editor && content !== editor.getHTML()) {
      // set editor content when state change externally
      editor.commands.setContent(content);
    }
  },[content]);

  return (<Stack>
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
    <Button disabled={editorContent === "" || editorContent === "<p></p>"} onClick={handleSubmit}>{btnLabel}</Button>
  </Stack>);
};


export default TextEditor;
