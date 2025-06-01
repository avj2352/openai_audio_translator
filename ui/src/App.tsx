import { Container, Title, Text, Stack } from '@mantine/core';
import { notifications } from '@mantine/notifications';
// ..custom
import { APP_VERSION } from "@/util/envConfig";
import '@/App.scss';
// import GradientCircularProgress from '@/components/GradientCircularProgress';
import YoutubeVideoInputForm from '@/components/YoutubeVideoInputForm';

function App() {

  // ..evt handlers
  const showNotification = () => {
    notifications.show({
      title: 'Success!',
      message: 'Mantine is working correctly',
      color: 'green',
    })
  }

  return (
    <Container className="app-container">
      <Stack gap="md">
        <div className="header">
          <Title order={1}>Audio Translator Demo <small>v{APP_VERSION}</small></Title>
          <Text c="dimmed" style={{marginBottom: 20}}>OpenAI agent to translate youtube / english audio files to hindi audio mp3</Text>
          <YoutubeVideoInputForm/>
        </div>
      </Stack>
    </Container>
  )
};

export default App;
