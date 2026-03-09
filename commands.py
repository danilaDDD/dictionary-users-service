from cmd_manager import ManagementCommandSystem

management_system = ManagementCommandSystem()
management_system.register(package="app.commands")
cli = management_system.create_cli()

if __name__ == '__main__':
    cli()