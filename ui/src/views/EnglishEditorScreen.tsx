import { type FC, type JSX, useContext } from 'react';
import { Text, Stack, Title } from '@mantine/core';
import { AppContext } from '@/services/AppContext';
import TextEditor from '@/components/TextEditor';
import type { ITranslateTextPayload } from '@/services/AudioApi';


const EnglishEditorScreen: FC = (): JSX.Element => {

  // ..states
  const { transcribedText, fetchTranslatedText } = useContext(AppContext);

  // ..evt handlers
  const handleTranslateText = (content: string) => {
    console.log('To translate: ', content);
    const payload: ITranslateTextPayload = {
      content,
      from_language: 'english',
      to_language: 'tamil'
    };
    fetchTranslatedText(payload);
  };

  return (<Stack>
    <Title order={2}>1. Transcribed Text</Title>
    <Text c="dimmed">
      AI is prone to make mistakes. Please review transcribed text below &
      modify accordingly*
    </Text>
    <TextEditor
      content={transcribedText}
      submitBtnLabel='Translate'
      onSubmit={handleTranslateText} />
  </Stack>);


};

export default EnglishEditorScreen;
