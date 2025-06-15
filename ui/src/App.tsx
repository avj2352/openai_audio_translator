import { Container, Title, Text, Stack } from '@mantine/core';
// ..custom
import { APP_VERSION } from "@/util/envConfig";
import '@/App.scss';
// import GradientCircularProgress from '@/components/GradientCircularProgress';
import YoutubeVideoInputForm from '@/views/YoutubeVideoInputForm';
import OpenAISVG from '@/components/OpenAISVG';
import EnglishEditorScreen from '@/views/EnglishEditorScreen';
import HindiEditorScreen from '@/views/HindiEditorScreen';

function App() {

  // ..evt handlers
  
  return (
    <Container className="app-container">
      <Stack gap="md">
        <div className="header">
          <Stack>
            <OpenAISVG width="200" height="100" fillColor='#07C8F9' />
            <Title order={1}>Audio Translator Demo <small>v{APP_VERSION}</small></Title>
          </Stack>
          <Text c="dimmed" style={{ marginBottom: 20 }}>OpenAI agent to translate youtube / english audio files to hindi audio mp3</Text>
          <YoutubeVideoInputForm />
          {/* english translator editor */}
          <EnglishEditorScreen/>
          {/* hindi translate editor */}
          <HindiEditorScreen/>
        </div>
      </Stack>
    </Container>
  )
};

export default App;
