import { ReactElement } from "react"
import AuthPage from "../pages/AuthPage/AuthPage"
import MainPage from "../pages/MainPage/MainPage"
import NotFoundPage from "../pages/NotFoundPage/NotFoundPage"
import SourcePage from "../pages/SourcePage/SourcePage"
import SourcesPage from "../pages/SourcesPage/SourcesPage"
import { AUTH_ROUTE, MAIN_ROUTE, SOURCES_ROUTE, SOURCE_ROUTE } from "../utils/constants"

class Route {
  constructor (public path: string, public element: ReactElement) {
    this.path = path
    this.element = element
  }
}

export const routes = [
  new Route(MAIN_ROUTE, <MainPage/>),
  new Route(AUTH_ROUTE, <AuthPage/>),
  new Route(SOURCE_ROUTE, <SourcePage/>),
  new Route(SOURCES_ROUTE, <SourcesPage/>),
  new Route('*', <NotFoundPage/>)
]