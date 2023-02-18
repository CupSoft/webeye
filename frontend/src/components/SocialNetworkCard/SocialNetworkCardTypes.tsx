export type SocialNetworkCardPropsType = {
  link: string;
  social: 'vk' | 'ok' | string;
  text: string;
  state: 'ok' | 'partial' | 'critical' | string;
}

export type IconsType = {
  [key: string]: string
}