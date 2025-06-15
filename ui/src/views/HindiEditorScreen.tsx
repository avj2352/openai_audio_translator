import { type FC, type JSX, useContext } from 'react';
import { Text, Stack, Title } from '@mantine/core';
import { AppContext } from '@/services/AppContext';
import TextEditor from '@/components/TextEditor';


const HindiEditorScreen: FC = (): JSX.Element => {

  // ..states
  const { translatedText } = useContext(AppContext);

  return (<Stack style={{marginTop: 20}}>
    <Title order={2}>1. Transcribed Text</Title>
    <Text c="dimmed">
      Please review the translated text*
    </Text>
    <TextEditor
      content={translatedText}
      submitBtnLabel='Generate'
      onSubmit={(content) => console.log('To translate: ', content)} />
  </Stack>);


};

export default HindiEditorScreen;
