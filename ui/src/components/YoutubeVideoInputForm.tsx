/**
* Youtube URL input form
*/
import { type FC, type JSX, useState } from 'react';
import { Button, Group, TextInput, Text } from "@mantine/core";
import { Flex, Title } from "@mantine/core";
import { useForm } from "@mantine/form";
// ..custom
import GradientCircularProgress from '@/components/GradientCircularProgress';




const YoutubeVideoInputForm: FC = (): JSX.Element => {
  // ..states
  const [isLoading, toggleLoading] = useState(false);
  // ..init form
  const form = useForm({
    initialValues: {
      // Default value for the file input
      url: 'https://www.youtube.com/watch?v=UbtP84vJIJ0',
      filename: ''
    },
    validate: {
      url: (value) => !isValidYouTubeVideoUrl(value) ? "a valid youtube link is required" : null,
      filename: (value) => value === "" ? "filename is required" : null,
    },
  });

  // ..evt handlers
  const handleFormSubmit = (values: { url: string, filename: string }) => {
    if (form.validate().hasErrors) return;
    const { url, filename } = values;
    toggleLoading(true);
  };

  // validate youtube url
  // More specific function for video URLs only
  function isValidYouTubeVideoUrl(url: string): boolean {
    if (!url || typeof url !== 'string') {
      return false;
    }

    const videoPatterns = [
      /^https?:\/\/(www\.)?youtube\.com\/watch\?v=[\w-]+/,
      /^https?:\/\/youtu\.be\/[\w-]+/,
      /^https?:\/\/(www\.)?youtube\.com\/embed\/[\w-]+/,
      /^https?:\/\/(www\.)?youtube\.com\/shorts\/[\w-]+/,
    ];

    return videoPatterns.some(pattern => pattern.test(url));
  }

  return (
    <Flex direction="column">
      <Title order={2}>Transcribe Youtube Video</Title>
      <Text c="dimmed" style={{marginBottom: 5}}>Please provide youtube url and name of the audio file in order to get the text content</Text>
      <form onSubmit={form.onSubmit(handleFormSubmit)}>
        {/* Row #1 */}
        <Group
          justify="flex-start"
          style={{ width: "100%", flexWrap: "wrap" }}
          gap={10}
          mb="md"
        >
          <TextInput
            style={{ flexGrow: 2 }}
            withAsterisk
            label="Youtube link"
            placeholder="Provide Youtube URL"
            key={form.key("url")}
            {...form.getInputProps("url")}
          />

          <TextInput
            style={{ flexGrow: 2 }}
            withAsterisk
            label="Audio Filename"
            placeholder="Enter audio filename"
            key={form.key("filename")}
            {...form.getInputProps("filename")}
          />

        </Group>
        {/* Row #2 */}
        <Group
          justify="flex-end"
          style={{ width: "100%", flexWrap: "wrap" }}
          gap={10}
          mb="md"
        >
          <Button
            onClick={() => form.reset()}
            type="reset" variant="default">Cancel</Button>
          <Button type="submit" disabled={isLoading}>Transcribe</Button>
        </Group>


      </form>
    <GradientCircularProgress isLoading={isLoading}/>
    </Flex>
  
  );
};

export default YoutubeVideoInputForm;
