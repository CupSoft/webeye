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

export type SourceDataTypes = {
  name: string;
  status: 'OK' | 'partial' | 'critical';
  uuid: string;
}

export type SourceGetTypes = {
  name: string;
  status: 'OK' | 'partial' | 'critical';
  uuid: string;
}

export type UserStoreTypes = {
  isAuth: boolean;
  isAdmin: boolean;
  email: string;
  uuid: string;
}