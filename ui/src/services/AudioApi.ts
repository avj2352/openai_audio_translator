import { AudioApiInstance } from "@/services/AudioApiInstance";

export type IYoutubeTranscribePayload = {
  url: string;
  filename: string;
};

const AudioApi = {
  postTranscribeYoutubeUrl: (
    payload: IYoutubeTranscribePayload
  ): Promise<any> => {
    console.log("translate youtube post data payload is: ", payload);
    return AudioApiInstance.post(`/transcribe/youtube`, payload);
  },
};

export default AudioApi;
