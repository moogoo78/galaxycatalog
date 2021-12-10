import React from 'react';
import ReactDOM from 'react-dom';

import {
  BrowserRouter,
  Routes,
  Route
} from 'react-router-dom';

//import DashboardIcon from '@mui/icons-material/Dashboard';
import YardIcon from '@mui/icons-material/Yard';
import PeopleIcon from '@mui/icons-material/People';
//import BarChartIcon from '@mui/icons-material/BarChart';
import HikingIcon from '@mui/icons-material/Hiking';
//import LayersIcon from '@mui/icons-material/Layers';

import AdminLayout from './AdminLayout';
import ListView from './ListView';
import FormView from './FormView';

const modelInfo = [
  //[<DashboardIcon />, 'Dashboard', '/admin/collection'],
  ['collection', <HikingIcon />, '採集資訊'],
  ['unit', <YardIcon />, '標本'],
  ['person', <PeopleIcon />, '採集者/鑑定者'],
];

function Admin() {
  return (
      <BrowserRouter>
      <Routes>
      <Route path="/admin" element=<AdminLayout modelInfo={modelInfo}/>>
        <Route path="collection" element=<ListView model="collection" /> />
        <Route path="/admin/collection/:itemId/edit" element={<FormView model="collection" label="採集資訊" />} />
        <Route path="/admin/person/:itemId/edit" element={<FormView model="person" label="採集者/鑑定者" />} />
        <Route path="unit" element=<ListView model="unit" /> />
        <Route path="person" element=<ListView model="person" /> />
        <Route path="collection:" element=<ListView model="person" /> />
      </Route>
      </Routes>
      </BrowserRouter>
  )
}

ReactDOM.render(<Admin />, document.querySelector('#hello'));
