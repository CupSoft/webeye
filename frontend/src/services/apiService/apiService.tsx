import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { ReviewGetTypes, SocialReporGetTypes, SourceGetTypes, SubscriptionGetRequestTypes, SubscriptionGetResponseTypes, SubscriptionPostTypes, UserLoginResponseTypes, UserRegistrRequestTypes, UserRegistrResponseTypes } from './apiServiceTypes'

export const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({
    baseUrl: process.env.REACT_APP_API_LINK,
    prepareHeaders(headers, {getState}) {
      const token = localStorage.getItem('token')

      if (token) {
        headers.set('Authorization', token)
      }

      return headers
    }
  }),
  tagTypes: ['User', 'Source'],
  endpoints: (builder) => ({
    registerUser: builder.mutation<UserRegistrResponseTypes, UserRegistrRequestTypes>({
      query: (user) => ({
        method: 'POST',
        url: 'auth/users',
        body: JSON.stringify(user),
        headers: {'Content-Type': 'application/json'}
      })
    }),
    loginUser: builder.mutation<UserLoginResponseTypes, FormData>({
      query: (user) => ({
        method: 'POST',
        url: 'auth/login/access-token',
        body: user,
        headers: {'Content-Type': undefined}
      })
    }),
    checkUser: builder.mutation<UserRegistrResponseTypes, void>({
      query: () => ({url: 'auth/users/me'})
    }),
    getSource: builder.query<SourceGetTypes, string>({
      query: (sourceUuid) => ({ url: `resources/${sourceUuid}` })
    }),
    getAllSources: builder.query<SourceGetTypes[], void>({
      query: () => ({ url: `resources`})
    }),
    getAllSocialReports: builder.query<SocialReporGetTypes[], string>({
      query: (sourceUuid) => ({ url: `resources/${sourceUuid}/social_reports`})
    }),
    getAllReviews: builder.query<ReviewGetTypes[], string>({
      query: (sourceUuid) => ({ url: `resources/${sourceUuid}/reviews` })
    }),
    postSubscriptions: builder.mutation<void, SubscriptionPostTypes>({
      query: ({userUuid, ...subs}) => ({
        method: 'POST',
        url: `subscriptions`,
        body: JSON.stringify(subs),
        headers: {'Content-Type': 'application/json'}
      })
    }),
    getSubscriptions: builder.mutation<SubscriptionGetResponseTypes, SubscriptionGetRequestTypes>({
      query: ({userUuid, sourceUuid}) => ({ url: `subscriptions?user_id=${userUuid}&resource_id=${sourceUuid}`})
    })
  })
})

export const { useRegisterUserMutation } = api
export const { useLoginUserMutation } = api
export const { useGetAllSourcesQuery } = api
export const { useGetSourceQuery } = api
export const { useCheckUserMutation } = api
export const { useGetAllSocialReportsQuery } = api
export const { useGetAllReviewsQuery } = api
export const { usePostSubscriptionsMutation } = api
export const { useGetSubscriptionsMutation } = api