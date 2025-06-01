import { Container, Title, Text, Stack } from '@mantine/core';
import { notifications } from '@mantine/notifications';
// ..custom
import { APP_VERSION } from "@/util/envConfig";
import '@/App.scss';

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
          <Text c="dimmed">OpenAI agent to translate youtube / english audio files to hindi audio mp3</Text>
        </div>
        
      </Stack>
    </Container>
  )
};

export default App;
