export type SocialNetworkBadgePropsType = {
  link: string;
  social_network: 'VK' | 'OK' | string;
  snippet: string;
  status: 'OK' | 'partial' | 'critical';
}

export type IconsType = {
  [key: string]: string
}