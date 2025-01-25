import QtQuick 2.15
import QtQuick.Controls 2.15
import Pyside_handler 1.0
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 600
    height: 600
    title: "CPU Monitor"

    Monitor {
        id: monitor_pyside
        // ready_queue_pyside
    }

    Rectangle {
        anchors.fill: parent
        anchors.margins: 20 // Adds spacing from the page borders
        color: "#f5f5f5" // Light gray background for contrast

        ColumnLayout {
            anchors.fill: parent
            spacing: 10 // Add spacing between rows

            // Header Rectangle
            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: parent.height / 6
                color: "lightblue"

                Text {
                    anchors.centerIn: parent
                    text: "RT Scheduling, Afshar-Safar"
                    font.pixelSize: 24
                    font.bold: true
                    color: "#000000"
                }
            }

            // Additional Info 1 Rectangle
            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: parent.height / 10
                color: "#cccccc" // Light gray color

                Text {
                    anchors.centerIn: parent
                    text: "Additional Info 1"
                    font.pixelSize: 18
                    color: "#333333" // Dark gray text
                }
            }

            // Additional Info 2 Rectangle
            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: parent.height / 10
                color: "#dddddd" // Slightly lighter gray

                Text {
                    anchors.centerIn: parent
                    text: "Additional Info 2"
                    font.pixelSize: 18
                    color: "#444444" // Slightly darker gray text
                }
            }

            // CPU1 Row
            RowLayout {
                Layout.fillWidth: true
                Layout.preferredHeight: parent.height / 12
                spacing: 10 // Space between text and progress bar

                Text {
                    text: "CPU1"
                    font.pixelSize: 16
                    Layout.alignment: Qt.AlignVCenter
                    Layout.preferredWidth: parent.width / 6
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignVCenter
                }

                ProgressBar {
                    Layout.fillWidth: true
                    id: sys1
                }
            }

            // CPU2 Row
            RowLayout {
                Layout.fillWidth: true
                Layout.preferredHeight: parent.height / 12
                spacing: 10

                Text {
                    text: "CPU2"
                    font.pixelSize: 16
                    Layout.alignment: Qt.AlignVCenter
                    Layout.preferredWidth: parent.width / 6
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignVCenter
                }

                ProgressBar {
                    Layout.fillWidth: true
                    id: sys2
                }
            }

            // CPU3 Row
            RowLayout {
                Layout.fillWidth: true
                Layout.preferredHeight: parent.height / 12
                spacing: 10

                Text {
                    text: "CPU3"
                    font.pixelSize: 16
                    Layout.alignment: Qt.AlignVCenter
                    Layout.preferredWidth: parent.width / 6
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignVCenter
                }

                ProgressBar {
                    Layout.fillWidth: true
                    id: sys3
                }
            }

            // CPU4 Row
            RowLayout {
                Layout.fillWidth: true
                Layout.preferredHeight: parent.height / 12
                spacing: 10

                Text {
                    text: "CPU4"
                    font.pixelSize: 16
                    Layout.alignment: Qt.AlignVCenter
                    Layout.preferredWidth: parent.width / 6
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignVCenter
                }

                ProgressBar {
                    Layout.fillWidth: true
                    id: sys4
                }
            }
        }
    }
    Row {
    spacing: 10
    anchors.fill: parent
    anchors.margins: 10

        Rectangle {
            width: parent.width
            height: 100
            color: "transparent"
            border.color: "black"
            border.width: 2
            radius: 10

            Row {
                spacing: 10
                anchors.fill: parent
                anchors.margins: 10

                Repeater {
                    model: monitor_pyside.ready_queue_subsys1_1
                    Rectangle {
                        width: 70
                        height: 50
                        color: "green" // Highlight the first task
                        border.color: "black"
                        border.width: 1
                        radius: 5
                        Text {
                            anchors.centerIn: parent
                            text: modelData
                            font.bold: index === 0
                        }
                    }
                }
            }
            // Text {
            //     anchors.bottom: parent.bottom
            //     anchors.horizontalCenter: parent.horizontalCenter
            //     anchors.margins: 5
            //     text: "Queue"
            //     font.pixelSize: 14
            // }
        }
    }
    Button {
        onClicked: console.log(monitor_pyside.ready_queue_subsys1_1)
    }
}
