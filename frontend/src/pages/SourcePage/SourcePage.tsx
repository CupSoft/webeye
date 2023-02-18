import { useParams } from 'react-router-dom';
import { Area, AreaChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import ReviewCard from '../../components/ReviewCard/ReviewCard';
import SocialNetworksCard from '../../components/SocialNetworksCard/SocialNetworksCard';
import SubscriptionCard from '../../components/SubscriptionCard/SubscriptionCard';
import Button from '../../components/UI/Button/Button';
import styles from './SourcePage.module.scss';
import cn from 'classnames'

const data = [
  {name: 'Page A',uv: 4000,pv: 2400,amt: 2400,},
  {name: 'Page B',uv: 3000,pv: 1398,amt: 2210,},
  {name: 'Page C',uv: 2000,pv: 9800,amt: 2290,},
  {name: 'Page D',uv: 2780,pv: 3908,amt: 2000,},
  {name: 'Page E',uv: 1890,pv: 4800,amt: 2181,},
  {name: 'Page F',uv: 2390,pv: 3800,amt: 2500},
  {name: 'Page G',uv: 3490,pv: 4300,amt: 2100,},
];

const sources = [
  {id: 1, name: 'Вышка', state: 'ok', rating: 4.92},
  {id: 2, name: 'МГТУ Баумана', state: 'critical', rating: 4.78},
  {id: 3, name: 'МФТИ', state: 'partial', rating: 4.95},
  {id: 4, name: 'Вышка', state: 'ok', rating: 4.92},
  {id: 5, name: 'МГТУ Баумана', state: 'critical', rating: 4.78},
  {id: 6, name: 'МФТИ', state: 'partial', rating: 4.95},
  {id: 7, name: 'Вышка', state: 'ok', rating: 4.92},
  {id: 8, name: 'МГТУ Баумана', state: 'critical', rating: 4.78},
  {id: 9, name: 'МФТИ', state: 'partial', rating: 4.95},
  {id: 10, name: 'МФТИ', state: 'partial', rating: 4.95},
]

const SourcePage = () => {
  const params = useParams()
  const id = params.id ? +params.id - 1 : -1
  const source = sources[id]

  function summaryClickHandler() {
    console.log('getSummary')
  }

  return (
    <div className={styles.container}>
      <div className={styles.title}>
        <h1 
          className={
            cn("page_title", styles.state, styles[source.state.toLowerCase()])
          }
        >
          {id !== -1 ? source.name : 'Ресурс'}
        </h1>
        <span className={styles.rating}>{source.rating}</span>
        <Button btnType='turquoise' onClick={summaryClickHandler}>
          <span className={styles.download_btn}>Получить отчёт</span>
        </Button>
      </div>
      <ResponsiveContainer width='100%' height={500}>
        <AreaChart
          className={styles.chart}
          data={data}
          margin={{
            top: 10,
            right: 30,
            left: 0,
            bottom: 0,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" stroke='#c5c5c5'/>
          <YAxis stroke='#c5c5c5'/>
          <Tooltip wrapperClassName={styles.chart_tooltip}/>
          <Area type="monotone" dataKey="uv" stroke="#8884d8" fill="#677cd9" />
        </AreaChart>
      </ResponsiveContainer>
      <div className={styles.cards}>
        <ReviewCard sourceId={source.id}/>
        <SocialNetworksCard sourceId={source.id}/>
        <SubscriptionCard sourceId={source.id}/>
      </div>
    </div>
  );
};

export default SourcePage;