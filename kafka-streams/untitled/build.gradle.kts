plugins {
    java
    kotlin("jvm") version "1.4.32"
}

group = "org.example"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    implementation(kotlin("stdlib"))
    testImplementation("org.junit.jupiter:junit-jupiter-api:5.6.0")
    testRuntimeOnly("org.junit.jupiter:junit-jupiter-engine")

    implementation("org.apache.kafka:kafka-streams:2.8.0")
    implementation("com.beust:klaxon:5.5")

    implementation("org.slf4j:slf4j-log4j12:1.7.30")

}


tasks.getByName<Test>("test") {
    useJUnitPlatform()
}