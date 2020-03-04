import Page from 'components/Page';
import React from 'react';
import {
  Button, Card, CardBody, CardImg, CardText, CardTitle,
  Col,
  Row,
} from 'reactstrap';

class HomePage extends React.Component {
  state = {
    persons: []
  };

  componentDidMount() {
    let component = this;
    fetch(process.env.REACT_APP_API_URL + 'persons').then(
      response => response.json()
    ).then(
      (persons) => {
        component.setState({persons});
      }
    ).catch(
      error => {console.log(error)}
    )
  }

  render() {
    return (
      <Page title="Accueil" breadcrumbs={[{ name: 'modals', active: true }]}>
        <Row>
          <Col lg={12} md={12} sm={12} xs={12} className="mb-3">
            <Card>
              <CardImg top src={require('../assets/img/map/arrondissements-paris-2.jpg')} />
            </Card>
          </Col>
        </Row>
        <Row>
          <Col lg="12" md="12" sm="12" xs="12">
            <Button color="primary" size="lg" block>
              Lancer le Random Lunch !
            </Button>
          </Col>
        </Row>
        <Row>
          {this.state.persons.map((person) => {
            return <Col lg={6} md={12} sm={12} xs={12} className="mb-3">
              <Card key={person.id} className="flex-row">
                {person.profile_picture &&
                <CardImg
                  className="card-img-left"
                  src={require('../assets/media/' + person.profile_picture)}
                  style={{ width: 'auto', height: 150 }}
                />}
                <CardBody>
                  <CardTitle>{person.first_name} {person.last_name}</CardTitle>
                  <CardText>
                    {person.location.name}<br/>{person.location.address}
                  </CardText>
                </CardBody>
              </Card>
            </Col>})}
        </Row>
      </Page>
    );
  }
}

export default HomePage;
