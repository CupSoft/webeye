import { Route, Routes } from "react-router-dom";
import { routes } from "../../router/routes";


const AppRouter = () => {
  return (
    <Routes>
      {routes.map(({path, element}) => 
        <Route key={path} path={path} element={element} />
      )}
    </Routes>
  );
};

export default AppRouter;