import * as React from 'react';
import ListItem from '@mui/material/ListItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import ListSubheader from '@mui/material/ListSubheader';
import DashboardIcon from '@mui/icons-material/Dashboard';
import YardIcon from '@mui/icons-material/Yard';
import PeopleIcon from '@mui/icons-material/People';
import BarChartIcon from '@mui/icons-material/BarChart';
import HikingIcon from '@mui/icons-material/Hiking';
import LayersIcon from '@mui/icons-material/Layers';
//import AssignmentIcon from '@mui/icons-material/Assignment';
import { Link as RouterLink } from "react-router-dom";

export const ModelList = () => {
  const modelInfo = [
    //[<DashboardIcon />, 'Dashboard', '/admin/collection'],
    [<HikingIcon />, '採集資訊', '/admin/collection'],
    [<YardIcon />, '標本', '/admin/unit'],
    [<PeopleIcon />, '採集者/鑑定者', '/admin/person'],
  ];
  return modelInfo.map((v, i)=>{
    return (
        <ListItem button component={RouterLink} to={v[2]} key={i}>
        <ListItemIcon>
        {v[0]}
        </ListItemIcon>
        <ListItemText primary={v[1]} />
        </ListItem>
    )
  });
}

export const mainListItems = (
  <div>
    <ListItem button>
      <ListItemIcon>
        <DashboardIcon />
      </ListItemIcon>
      <ListItemText primary="Dashboard" />
    </ListItem>
    <ListItem button component={RouterLink} to="/admin/collection">
      <ListItemIcon>
        <HikingIcon />
      </ListItemIcon>
      <ListItemText primary="採集" />
    </ListItem>
    <ListItem button component={RouterLink} to="/admin/unit">
      <ListItemIcon>
        <YardIcon />
      </ListItemIcon>
      <ListItemText primary="標本" />
    </ListItem>
    <ListItem button component={RouterLink} to="/admin/person">
      <ListItemIcon>
        <PeopleIcon />
      </ListItemIcon>
      <ListItemText primary="採集者/鑑定者" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <BarChartIcon />
      </ListItemIcon>
      <ListItemText primary="Reports" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <LayersIcon />
      </ListItemIcon>
      <ListItemText primary="Integrations" />
    </ListItem>
  </div>
);
