var frisby = require("frisby"),
//    hereweb = "https://dv.hereweb.here.com";
    hereweb = "https://experiment-dv.hereweb.here.com";

frisby
    .create('HTML pages should not be cached, since they contain configuration and IP lookup that differs per client')
    .get(hereweb + "/", {followRedirect: false})
    .expectStatus(200)
    .expectHeaderContains('Cache-Control', 'no-store')
    .expectHeaderContains('Cache-Control', 'must-revalidate')
    .toss();

frisby
    .create('HTML pages non-root should not be cached')
    .get(hereweb + "/directions?map=52.2401,6.17503,13,normal", {followRedirect: false})
    .expectStatus(200)
    .expectHeaderContains('Cache-Control', 'no-store')
    .expectHeaderContains('Cache-Control', 'must-revalidate')
    .toss();

frisby
    .create('API urls should not be cached')
    .get(hereweb + "/api/photos/48.88979/2.3412/AND/Day,Summer/RAIN", {followRedirect: false})
    .expectStatus(200)
    .expectHeaderContains('Cache-Control', 'no-store')
    .expectHeaderContains('Cache-Control', 'must-revalidate')
    .toss();

// not. not supported...
//frisby
//    .create('CSS files should be cached')
//    .get(hereweb + "/style.css", {followRedirect: false})
//    .expectStatus(200)
//    not.expectHeaderContains('Cache-Control', 'no-store')
//    not.expectHeaderContains('Cache-Control', 'must-revalidate')
//    .toss();

// Business pages caching / lang redirects
// Hitting the cache takes a mx of 3 attempts
var rnd = Math.random();

frisby
    .create('Business page redirects should not be cached')
    .get(hereweb + "/abouthere/?rnd=" + rnd, {followRedirect: false})
		.addHeader("Accept-Language", "fr-FR")
    .expectStatus(301)
    .expectHeaderContains('Location', '/abouthere/?rnd=' + rnd + '&lang=fr-FR')

    .get(hereweb + "/abouthere/?rnd=" + rnd, {followRedirect: false})
		.addHeader("Accept-Language", "fr-FR")
    .expectStatus(301)
    .expectHeaderContains('Location', '/abouthere/?rnd=' + rnd + '&lang=fr-FR')

    .get(hereweb + "/abouthere/?rnd=" + rnd, {followRedirect: false})
		.addHeader("Accept-Language", "fr-FR")
    .expectStatus(301)
    .expectHeaderContains('Location', '/abouthere/?rnd=' + rnd + '&lang=fr-FR')

    .get(hereweb + "/abouthere/?rnd=" + rnd, {followRedirect: false})
		.addHeader("Accept-Language", "de-DE")
    .expectStatus(301)
    .expectHeaderContains('Location', '/abouthere/?rnd=' + rnd + '&lang=de-DE')

		.toss();
