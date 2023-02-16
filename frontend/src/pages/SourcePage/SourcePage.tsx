import { useParams } from 'react-router-dom';
import { LineChart, Line, CartesianGrid, XAxis, YAxis } from 'recharts';
import styles from './SourcePage.module.scss'

const SourcePage = () => {
  const params = useParams()
  const data = [
    {name: 'Page A', uv: 400, pv: 2400, amt: 2400},
    {name: 'Page B', uv: 300, pv: 500, amt: 2400},
    {name: 'Page C', uv: 0, pv: 200, amt: 2400},
    {name: 'Page D', uv: 200, pv: 2400, amt: 2400},
    {name: 'Page E', uv: 200, pv: 100, amt: 2400},
  ];

  return (
    <div>
      {`Source: ${params.id}`}
      <LineChart width={300} height={300} data={data}>
        <Line type="monotone" dataKey="uv" stroke="#8884d8" />
        <CartesianGrid stroke="#ccc" />
        <XAxis dataKey="name" />
        <YAxis />
      </LineChart>
    </div>
  );
};

export default SourcePage;