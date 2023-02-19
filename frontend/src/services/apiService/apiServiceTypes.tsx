export type UserRegistrResponseTypes = {
  email: string;
  uuid: string;
  is_admin: boolean;
}

export type UserRegistrRequestTypes = {
  email: string;
  password: string;
}

export type UserLoginResponseTypes = {
  access_token: string,
  token_type: string,
}

export type SourceGetTypes = {
  name: string;
  status: 'OK' | 'partial' | 'critical';
  uuid: string;
  rating: number;
}

export type UserStoreTypes = {
  isAuth: boolean;
  isAdmin: boolean;
  email: string;
  uuid: string;
}

export type SocialReporGetTypes = {
  status: 'OK' | 'partial' | 'critical';
  social_network: 'VK' | 'OK',
  link: string;
  uuid: string;
  created_at: string;
  snippet: string
  resource_uuid?: string;
}

export type ReviewGetTypes = {
  datatime: string;
  text: string;
  stars: number;
  uuid: string;
}

export type SubscriptionPostTypes = {
  to_telegram: boolean;
  to_email: boolean;
  resource_uuid: string;
}

export type SubscriptionGetResponseTypes = {
  to_telegram: boolean;
  to_email: boolean;
  uuid?: string;
}